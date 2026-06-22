def sum_digits(number):
    digit_strings = list(str(abs(number)))
    digit_integers = list(map(int, digit_strings))
    return sum(digit_integers)

if __name__ == '__main__':
    sample_value = 40592
    result = sum_digits(sample_value)
    print(result)