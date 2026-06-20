def is_positive_even_divisible_by_three(num):
    return num > 0 and num % 2 == 0 and num % 3 == 0

if __name__ == '__main__':
    sample_values = [6, -4, 9, 15, 0]
    for value in sample_values:
        print(f"{value}: {is_positive_even_divisible_by_three(value)}")