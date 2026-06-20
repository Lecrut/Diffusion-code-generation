def is_positive_even_and_divisible_by_three(number):
    return number > 0 and number % 2 == 0 and number % 3 == 0

if __name__ == '__main__':
    sample_value = 18
    result = is_positive_even_and_divisible_by_three(sample_value)
    print(result)