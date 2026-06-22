def compare_weights(weight1, unit1, weight2, unit2):
    kg_to_lbs = 0.453592
    
    if unit1 == 'kg':
        weight1 *= kg_to_lbs
    elif unit1 != 'lbs':
        raise ValueError("Invalid unit for weight1")
    
    if unit2 == 'kg':
        weight2 /= kg_to_lbs
    elif unit2 != 'lbs':
        raise ValueError("Invalid unit for weight2")
    
    if weight1 > weight2:
        return f"{weight1:.2f} lbs is heavier than {weight2:.2f} kg"
    elif weight1 < weight2:
        return f"{weight2:.2f} kg is heavier than {weight1:.2f} lbs"
    else:
        return "Both weights are equal"

if __name__ == '__main__':
    print(compare_weights(10, 'kg', 2.20462, 'lbs'))