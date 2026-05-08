def determine_category(value, thresholds):
    if value < thresholds[0]:
        return 0
    elif value < thresholds[1]:
        return 1
    elif value < thresholds[2]:
        return 2
    else:
        return 3
if __name__ == '__main__':
    test_value_1 = 5
    test_thresholds_1 = [10, 20, 30]
    result_1 = determine_category(test_value_1, test_thresholds_1)
    print(f"Value: {test_value_1}, Thresholds: {test_thresholds_1}, Category: {result_1}")
    test_value_2 = 15
    test_thresholds_2 = [10, 20, 30]
    result_2 = determine_category(test_value_2, test_thresholds_2)
    print(f"Value: {test_value_2}, Thresholds: {test_thresholds_2}, Category: {result_2}")
    test_value_3 = 35
    test_thresholds_3 = [10, 20, 30]
    result_3 = determine_category(test_value_3, test_thresholds_3)
    print(f"Value: {test_value_3}, Thresholds: {test_thresholds_3}, Category: {result_3}")
    test_value_4 = 9
    test_thresholds_4 = [10, 20, 30]
    result_4 = determine_category(test_value_4, test_thresholds_4)
    print(f"Value: {test_value_4}, Thresholds: {test_thresholds_4}, Category: {result_4}")