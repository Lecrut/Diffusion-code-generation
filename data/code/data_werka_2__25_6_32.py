def contains_zero(numbers):
    return 0 in numbers

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    ANOTHER_SAMPLE_LIST = [-10, -20, -30, 0, -40]

    result1 = contains_zero(SAMPLE_LIST)
    result2 = contains_zero(ANOTHER_SAMPLE_LIST)

    print(result1)
    print(result2)