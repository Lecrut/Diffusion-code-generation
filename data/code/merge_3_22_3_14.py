num = 17; print('odd' if num % 2 else 'even')
if __name__ == '__main__':
    # Check odd numbers with hardcoded sample values
    test_cases = [10, 13, 5]
    for n in test_cases:
        result = 'odd' if n % 2 else 'even'
        print(f"{n}: {result}")