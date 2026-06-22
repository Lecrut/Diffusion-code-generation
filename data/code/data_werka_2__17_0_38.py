def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [10, 15, 20, 25, -30]
    for val in test_values:
        print(f"{val} is even: {is_even(val)}")