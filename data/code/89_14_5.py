def calculator(num1, num2, operation):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        raise ValueError(f"Unsupported operation: {operation}")
def main():
    num1 = 20
    num2 = 5
    operation = "*"
    try:
        result = calculator(num1, num2, operation)
        print(f"Result of {num1} {operation} {num2} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()