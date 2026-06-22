def sum_of_digits(n: int) -> int:
    return sum([int(digit) for digit in str(n)])

if __name__ == '__main__':
    sample_number_1 = 12345
    sample_number_2 = 987654321
    result_1 = sum_of_digits(sample_number_1)
    result_2 = sum_of_digits(sample_number_2)
    print(result_1)
    print(result_2)