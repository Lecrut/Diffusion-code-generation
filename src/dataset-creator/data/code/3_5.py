def is_even(n: int) -> bool:
    return n % 2 == 0
if __name__ == '__main__':
    test_cases = [-5, -4, 3, 17, 0]
    for num in test_cases:
        print(f"{num} is {'even' if is_even(num) else 'odd'}")