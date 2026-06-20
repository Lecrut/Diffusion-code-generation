def perform_arithmetic():
    a = 20
    b = 4

    addition_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b
    division_result = a / b if b != 0 else float('inf')

    return addition_result, subtraction_result, multiplication_result, division_result

if __name__ == '__main__':
    results = perform_arithmetic()
    print(f"Addition: {results[0]}")
    print(f"Subtraction: {results[1]}")
    print(f"Multiplication: {results[2]}")
    print(f"Division: {results[3]}")