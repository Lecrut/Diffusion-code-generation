def is_odd(num):
    return num % 2 != 0

if __name__ == '__main__':
    test_cases = [4, 5, -3, 10]
    results = []
    for n in test_cases:
        result = is_odd(n)
        print(f"is_odd({n}) = {result}")