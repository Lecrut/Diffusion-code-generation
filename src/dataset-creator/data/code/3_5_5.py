def is_even(n: int) -> bool:
    return n % 2 == 0
if __name__ == '__main__':
    test_cases = [-5, -4, 3, 10]
    for val in test_cases:
        print(f"{val} is {'even' if is_even(val) else 'odd'}")