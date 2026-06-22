def sum_digits(number):
    return sum(map(int, str(abs(number))))

if __name__ == '__main__':
    sample_number = 12345
    print(sum_digits(sample_number))