def compare_weights(weight1, unit1, weight2, unit2):
    conversion_factor = 0.453592
    if unit1 == 'kg':
        weight1_in_kg = weight1
    elif unit1 == 'lbs':
        weight1_in_kg = weight1 * conversion_factor
    else:
        raise ValueError("Invalid unit for weight1")

    if unit2 == 'kg':
        weight2_in_kg = weight2
    elif unit2 == 'lbs':
        weight2_in_kg = weight2 * conversion_factor
    else:
        raise ValueError("Invalid unit for weight2")

    if weight1_in_kg > weight2_in_kg:
        return f"{weight1} {unit1} is heavier than {weight2} {unit2}"
    elif weight1_in_kg < weight2_in_kg:
        return f"{weight2} {unit2} is heavier than {weight1} {unit1}"
    else:
        return f"{weight1} {unit1} and {weight2} {unit2} are equal"

if __name__ == '__main__':
    print(compare_weights(50, 'kg', 110, 'lbs'))
    print(compare_weights(70, 'kg', 154, 'lbs'))
    print(compare_weights(68, 'kg', 150, 'lbs'))