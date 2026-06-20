def perform_arithmetic():
    a = 20
    b = 4
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else float('inf')
    return addition, subtraction, multiplication, division

if __name__ == '__main__':
    results = perform_arithmetic()
    print(f"Addition: {results[0]}")
    print(f"Subtraction: {results[1]}")
    print(f"Multiplication: {results[2]}")
    print(f"Division: {results[3]:.5f}")