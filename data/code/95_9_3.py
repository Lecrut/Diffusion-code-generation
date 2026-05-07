def check_number_properties(number):
    is_positive = number > 0
    is_even = number % 2 == 0
    is_divisible_by_5 = number % 5 == 0
    return is_positive, is_even, is_divisible_by_5
if __name__ == '__main__':
    test_numbers = [10, -5, 7, 25, 0, 12]
    for num in test_numbers:
        positive, even, div_5 = check_number_properties(num)
        print(f"Number: {num}")
        print(f"  Is Positive: {positive}")
        print(f"  Is Even: {even}")
        print(f"  Divisible by 5: {div_5}")
        print("-" * 10)