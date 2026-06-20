def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    operations = {
        'add': (5, 3),
        'subtract': (10, 4)
    }
    
    for operation, (x, y) in operations.items():
        if operation == 'add':
            result = add(x, y)
        elif operation == 'subtract':
            result = subtract(x, y)
        
        print(f'{operation.capitalize()}: {result}')