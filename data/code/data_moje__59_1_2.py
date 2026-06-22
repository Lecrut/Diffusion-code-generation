def sum_digits(number):
    return sum(map(int, str(number)))

if __name__ == '__main__':
    sample_number = 12345
    result = sum_digits(sample_number)
    print(result)