def evaluate_and_operation(num1, num2):
    if not isinstance(num1, bool) or not isinstance(num2, bool):
        raise ValueError("Both arguments must be boolean values")
    return num1 & num2

if __name__ == '__main__':
    result = evaluate_and_operation(True, False)
    print(f"True AND False = {result}")