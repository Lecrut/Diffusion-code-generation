def perform_operations(a, b):
    return a + b, a - b

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    add_result, subtract_result = perform_operations(num1, num2)
    print(f"Addition: {add_result}")
    print(f"Subtraction: {subtract_result}")