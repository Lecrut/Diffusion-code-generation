def multiply_numbers(a: int, b: int) -> float:
    try:
        return a * b
    except Exception as e:
        raise RuntimeError(f"Error during multiplication: {e}") from e
if __name__ == '__main__':
    num1 = 42
    num2 = 37
    result = multiply_numbers(num1, num2)
    print(result)