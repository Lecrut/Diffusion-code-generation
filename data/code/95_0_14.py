THRESHOLD_ZERO = 0
DIVISOR_TEN = 10
DIVISOR_THREE = 3

def evaluate_integer(n):
    is_positive = n > THRESHOLD_ZERO
    is_even = n % DIVISOR_TEN == 0
    is_divisible_by_three = n % DIVISOR_THREE == 0
    return is_positive, is_even, is_divisible_by_three

if __name__ == '__main__':
    numbers_to_check = [10, 15, -4, 6]
    for num in numbers_to_check:
        result = evaluate_integer(num)
        print(result)