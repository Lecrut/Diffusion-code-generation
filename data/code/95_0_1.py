def check_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_divisible_by_three = n % 3 == 0
    return is_positive, is_even, is_divisible_by_three
if __name__ == '__main__':
    sample_numbers = [10, 11, 12, -5, 6]
    for number in sample_numbers:
        positive, even, divisible_by_three = check_number(number)
        print(f"Number: {number}, Positive: {positive}, Even: {even}, Divisible by 3: {divisible_by_three}")