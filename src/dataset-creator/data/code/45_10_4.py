def calculate_sum(a: float, b: float) -> float:
    try:
        return a + b
    except TypeError as e:
        raise ValueError("Invalid inputs provided.") from e
if __name__ == '__main__':
    num1 = 5.0
    num2 = 3.0
    result = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")