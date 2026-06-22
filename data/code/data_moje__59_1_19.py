DIGIT_SEPARATOR = ''
DEFAULT_INPUT = 9876

def compute_digit_sum(value):
    str_value = str(value)
    if DIGIT_SEPARATOR in str_value:
        clean_str = str_value.replace(DIGIT_SEPARATOR, '')
    else:
        clean_str = str_value
    digits = map(int, clean_str)
    total = 0
    for d in digits:
        total += d
    return total

if __name__ == '__main__':
    result = compute_digit_sum(DEFAULT_INPUT)
    print(result)