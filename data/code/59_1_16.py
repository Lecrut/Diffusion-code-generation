def sum_of_digits(number):
    return sum(map(int, str(number)))

if __name__ == '__main__':
    example_number = 12345
    print(sum_of_digits(example_number))