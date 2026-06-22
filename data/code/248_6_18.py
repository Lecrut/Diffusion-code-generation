def add_two_numbers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return a + b

if __name__ == '__main__':
    result1 = add_two_numbers(5, 3)
    print(f"The sum is: {result1}")
    result2 = add_two_numbers(-1, 7)
    print(f"The sum is: {result2}")