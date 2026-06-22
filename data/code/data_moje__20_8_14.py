def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, -1, 2, -2, 3, -3, 4, -4, 100, -100, 99, -99]
    for value in test_values:
        print(f"is_even({value}) = {is_even(value)}")