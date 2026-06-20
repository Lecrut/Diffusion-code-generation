def is_positive_even_divisible_by_three(number):
    return number > 0 and number % 2 == 0 and (number % 3 == 0)
if __name__ == '__main__':
    print(is_positive_even_divisible_by_three(6))
    print(is_positive_even_divisible_by_three(-4))
    print(is_positive_even_divisible_by_three(9))
    print(is_positive_even_divisible_by_three(12))