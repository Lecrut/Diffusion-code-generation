def validate_positive_even_divisible(numbers):
    qualifying_count = 0
    for value in numbers:
        if value > 0 and value % 2 == 0:
            qualifying_count += 1
    return qualifying_count >= 3

if __name__ == '__main__':
    test_set_1 = [4, 8, 12, -1, 0, 3]
    test_set_2 = [-2, -4, -6, -8, -10]
    test_set_3 = [1, 3, 5, 7, 9, 11]
    test_set_4 = [2, 4, 6, 8, 10, 12]
    result_a = validate_positive_even_divisible(test_set_1)
    result_b = validate_positive_even_divisible(test_set_2)
    result_c = validate_positive_even_divisible(test_set_3)
    result_d = validate_positive_even_divisible(test_set_4)
    print(result_a)
    print(result_b)
    print(result_c)
    print(result_d)