def compare_weights(weight1, unit1, weight2, unit2):
    kg_per_lb = 0.453592
    if unit1 == 'kg':
        weight1_kg = weight1
    elif unit1 == 'lbs':
        weight1_kg = weight1 * kg_per_lb
    else:
        raise ValueError("Unsupported unit for weight1")
    
    if unit2 == 'kg':
        weight2_kg = weight2
    elif unit2 == 'lbs':
        weight2_kg = weight2 * kg_per_lb
    else:
        raise ValueError("Unsupported unit for weight2")
    
    if weight1_kg > weight2_kg:
        return f"{weight1} {unit1} is heavier than {weight2} {unit2}"
    elif weight1_kg < weight2_kg:
        return f"{weight2} {unit2} is heavier than {weight1} {unit1}"
    else:
        return f"Both weights are equal: {weight1} {unit1}"

if __name__ == '__main__':
    result = compare_weights(70, 'kg', 154, 'lbs')
    print(result)