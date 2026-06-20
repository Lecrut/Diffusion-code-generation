def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    operations = {
        'add': (5, 3),
        'subtract': (10, 4)
    }
    
    for operation, values in operations.items():
        if operation == 'add':
            print(f"Addition of {values[0]} and {values[1]}: {add_numbers(*values)}")
        elif operation == 'subtract':
            print(f"Subtraction of {values[0]} and {values[1]}: {subtract_numbers(*values)}")