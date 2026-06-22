def is_larger(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    SAMPLE_VALUES = [(10, 5), (3, 7), (-1, -5), (0, 0), (5.5, 2)]
    for value1, value2 in SAMPLE_VALUES:
        print(is_larger(value1, value2))