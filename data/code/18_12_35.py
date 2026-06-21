def is_greater(a, b):
    return a > b
if __name__ == '__main__':
    first_value = 20
    second_value = 15
    result = is_greater(first_value, second_value)
    print(result)
    another_first_value = -5
    another_second_value = -10
    another_result = is_greater(another_first_value, another_second_value)
    print(another_result)
    equal_values = 7
    equal_result = is_greater(equal_values, equal_values)
    print(equal_result)
    reverse_order = 3
    reverse_result = is_greater(reverse_order, 8)
    print(reverse_result)