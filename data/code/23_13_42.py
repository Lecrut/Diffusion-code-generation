def compare_values(value1, value2):
    comparison_map = {
        "greater": value1 > value2,
        "less": value1 < value2,
        "equal": value1 == value2
    }
    
    for key, condition in comparison_map.items():
        if condition:
            return f"First value is {key} than the second value."

if __name__ == '__main__':
    sample_value1 = 50
    sample_value2 = 30
    result = compare_values(sample_value1, sample_value2)
    print(result)