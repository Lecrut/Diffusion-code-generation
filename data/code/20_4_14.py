def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [2, 7, 0, -4, -3, 15, 100]
    for value in test_cases:
        print(f"is_even({value}) = {is_even(value)}")