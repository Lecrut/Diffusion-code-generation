def multiply_integers(a: int, b: int) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    return a * b
if __name__ == '__main__':
    num1 = -5
    num2 = 3.0
    try:
        result = multiply_integers(num1, num2)
        print(f"The product of {num1} and {num2} is {result}")
        zero_test = multiply_integers(0, -42)
        print(f"Zero multiplication: 0 * {-42} = {zero_test}")
        negative_negative = multiply_integers(-10, -7)
        print(f"Negative times Negative: {-10} * {-7} = {negative_negative}")
    except TypeError as e:
        print(f"Error occurred during multiplication: {e}")