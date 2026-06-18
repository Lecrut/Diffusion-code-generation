is_even = num % 2 == 0 if isinstance(num, int) else False

if __name__ == '__main__':
    test_values = [4, 7, -2, "5", None]
    results = [(num, is_even) for num in test_values]
    print("Results:", results)