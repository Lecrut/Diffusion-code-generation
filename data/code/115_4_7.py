def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    result = divide_numbers(10.0, 2.0)
    print(result)