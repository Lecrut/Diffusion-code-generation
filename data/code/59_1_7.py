DIGIT_MAP = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def sum_digits(number):
    digits = str(abs(number))
    mapped_values = map(lambda char: DIGIT_MAP[char], digits)
    return sum(mapped_values)

if __name__ == '__main__':
    sample_value = 87654
    computed_sum = sum_digits(sample_value)
    print(computed_sum)