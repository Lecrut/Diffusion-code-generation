def is_greater(a, b):
    return a > b

if __name__ == '__main__':
    first_value = 15
    second_value = 7
    result = is_greater(first_value, second_value)
    print(result)

    first_value = 2
    second_value = 4
    result = is_greater(first_value, second_value)
    print(result)

    first_value = -3
    second_value = -6
    result = is_greater(first_value, second_value)
    print(result)

    first_value = 0
    second_value = 0
    result = is_greater(first_value, second_value)
    print(result)