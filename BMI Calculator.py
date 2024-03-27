def calculate_bmi(weight, height, weight_unit):
    if weight_unit.lower() == "kg":
        bmi = weight / (height ** 2)
    elif weight_unit.lower() == "lbs":
        bmi = (weight / (height ** 2)) * 703
    else:
        raise ValueError("Invalid weight unit. Use 'kg' or 'lbs'.")

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    elif bmi >= 30.0:
        return "Obese"
    else:
        return "Invalid BMI"