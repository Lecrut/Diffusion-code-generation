def convert_lbs_to_kg(pounds):
    if not isinstance(pounds, (int, float)):
        raise TypeError("Input must be a number")
    return pounds * 0.453592

def compare_weights(weight1, unit1, weight2, unit2):
    if unit1 == 'kg':
        weight1_kg = weight1
    elif unit1 == 'lbs':
        weight1_kg = convert_lbs_to_kg(weight1)
    else:
        raise ValueError("Invalid unit for weight1")
    
    if unit2 == 'kg':
        weight2_kg = weight2
    elif unit2 == 'lbs':
        weight2_kg = convert_lbs_to_kg(weight2)
    else:
        raise ValueError("Invalid unit for weight2")
    
    if weight1_kg > weight2_kg:
        return f"{weight1} {unit1} is heavier than {weight2} {unit2}"
    elif weight1_kg < weight2_kg:
        return f"{weight2} {unit2} is heavier than {weight1} {unit1}"
    else:
        return f"{weight1} {unit1} and {weight2} {unit2} are equal"

if __name__ == '__main__':
    print(compare_weights(10, 'kg', 2.20462, 'lbs'))
    print(compare_weights(5, 'kg', 11, 'lbs'))
    print(compare_weights(7, 'kg', 7, 'kg'))