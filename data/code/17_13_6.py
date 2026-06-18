def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [4, 7, -18, 3]
    for val in test_values:
        print(f"Number {val} is even: {is_even(val)}")