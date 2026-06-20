def validate_operation(operation):
    if operation not in ['add', 'subtract']:
        raise ValueError("Invalid operation specified")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    
    validate_operation('add')
    result_add = add(num1, num2)
    print(f"Addition: {result_add}")
    
    validate_operation('subtract')
    result_subtract = subtract(num1, num2)
    print(f"Subtraction: {result_subtract}")