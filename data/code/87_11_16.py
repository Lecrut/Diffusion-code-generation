def evaluate_conditions(value1, value2):
    condition_1 = value1 > 5
    condition_2 = value2 < 10
    combined_result = condition_1 and condition_2
    return combined_result

if __name__ == '__main__':
    test_value1 = 6
    test_value2 = 8
    result = evaluate_conditions(test_value1, test_value2)
    print(result)