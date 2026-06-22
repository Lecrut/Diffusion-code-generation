def sum_digits(number):
    if number < 0:
        number = -number
    return sum(map(int, str(number)))

if __name__ == '__main__':
    TEST_VALUE = 9876
    print(sum_digits(TEST_VALUE))