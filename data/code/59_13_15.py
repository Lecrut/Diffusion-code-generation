def sum_of_digits(n: int) -> int:
    digit_strings = list(str(n))
    digit_ints = [int(char) for char in digit_strings]
    return sum(digit_ints)

if __name__ == '__main__':
    test_number = 864209
    calculated_sum = sum_of_digits(test_number)
    print(calculated_sum)
    test_number_two = 55555
    calculated_sum_two = sum_of_digits(test_number_two)
    print(calculated_sum_two)