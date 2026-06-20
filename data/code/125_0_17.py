def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    operations = {
        'add': (5, 3),
        'subtract': (10, 4)
    }
    
    for operation, (num1, num2) in operations.items():
        if operation == 'add':
            result = add(num1, num2)
            print(f"Addition of {num1} and {num2} is: {result}")
        elif operation == 'subtract':
            result = subtract(num1, num2)
            print(f"Subtraction of {num1} and {num2} is: {result}")