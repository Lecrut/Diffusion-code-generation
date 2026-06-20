def is_positive_even_divisible_by_three(number):
    return number > 0 and number % 2 == 0 and number % 3 == 0

if __name__ == '__main__':
    sample_number = 6
    print(is_positive_even_divisible_by_three(sample_number))