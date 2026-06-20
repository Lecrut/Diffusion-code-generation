def check_number(n):
    IS_POSITIVE = n > 0
    IS_EVEN = n % 2 == 0
    IS_DIVISIBLE_BY_THREE = n % 3 == 0
    return IS_POSITIVE, IS_EVEN, IS_DIVISIBLE_BY_THREE

if __name__ == '__main__':
    SAMPLE_NUMBERS = [10, 15, -4, 6]
    for number in SAMPLE_NUMBERS:
        positive, even, divisible_by_three = check_number(number)
        print(f"Number: {number}, Positive: {positive}, Even: {even}, Divisible by 3: {divisible_by_three}")