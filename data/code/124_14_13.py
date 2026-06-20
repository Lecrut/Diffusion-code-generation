def arithmetic_operations(a=5.0, b=2.0):
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b if b != 0 else 'Error: Division by zero'
        return addition, subtraction, multiplication, division
    except Exception as e:
        return f'An error occurred: {e}'

if __name__ == '__main__':
    result = arithmetic_operations()
    print(f'Addition: {result[0]}')
    print(f'Subtraction: {result[1]}')
    print(f'Multiplication: {result[2]}')
    print(f'Division: {result[3]}')