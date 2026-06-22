def verify_positive_even_divisibility(values):
    qualifying_count = 0
    threshold = 3
    for current_value in values:
        is_positive = current_value > 0
        is_even = current_value % 2 == 0
        is_divisible_by_two = current_value % 2 == 0
        if is_positive and is_even and is_divisible_by_two:
            qualifying_count += 1
    return qualifying_count >= threshold

if __name__ == '__main__':
    test_data_a = [4, 6, 8, 10, 12]
    test_data_b = [-2, 0, 1, 3, 5]
    test_data_c = [2, 4, 1, 3, 5, 7]
    test_data_d = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    result_a = verify_positive_even_divisibility(test_data_a)
    result_b = verify_positive_even_divisibility(test_data_b)
    result_c = verify_positive_even_divisibility(test_data_c)
    result_d = verify_positive_even_divisibility(test_data_d)
    
    print(result_a)
    print(result_b)
    print(result_c)
    print(result_d)