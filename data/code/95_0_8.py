def is_positive_even_divisible_by_three(num):
    return num > 0 and num % 2 == 0 and (num % 3 == 0)
if __name__ == '__main__':
    print(is_positive_even_divisible_by_three(6))
    print(is_positive_even_divisible_by_three(-4))
    print(is_positive_even_divisible_by_three(9))