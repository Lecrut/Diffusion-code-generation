def add_numbers(a: int, b: int) -> None:
    try:
        result = a + b
        print(result)
    except TypeError as e:
        raise ValueError("Both inputs must be integers.") from e
if __name__ == '__main__':
    num1 = 5
    num2 = 3
    add_numbers(num1, num2)