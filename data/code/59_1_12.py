NUMERIC_BASE = 10
DEFAULT_SAMPLE = 78901

def sum_digits(number):
    str_value = str(abs(number))
    digit_iterator = map(int, str_value)
    return sum(digit_iterator)

if __name__ == '__main__':
    test_input = DEFAULT_SAMPLE
    output = sum_digits(test_input)
    print(output)