def is_even(n: int) -> bool:
    return n % 2 == 0
if __name__ == '__main__':
    test_cases = [-5, -4, 3, 0, 10]
    for num in test_cases:
        result = "Even" if is_even(num) else "Odd"
        print(f"{num} is {result}")