def is_positive_even_divisible_by_three(number):
    return number > 0 and number % 2 == 0 and number % 3 == 0

if __name__ == '__main__':
    sample_values = [6, -4, 9, 15, 0]
    for value in sample_values:
        print(is_positive_even_divisible_by_three(value))