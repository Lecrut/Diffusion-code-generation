def compare_values(value1, value2):
    comparison_map = {
        "greater": f"First value is greater than the second value.",
        "less": f"First value is less than the second value.",
        "equal": f"First value is equal to the second value."
    }
    
    if value1 > value2:
        return comparison_map["greater"]
    elif value1 < value2:
        return comparison_map["less"]
    else:
        return comparison_map["equal"]

if __name__ == '__main__':
    first_value = 30
    second_value = 60
    result = compare_values(first_value, second_value)
    print(result)