import math

def calculate_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else 'undefined'
    power = math.pow(a, b)
    square_root_a = math.sqrt(a) if a >= 0 else 'undefined'
    square_root_b = math.sqrt(b) if b >= 0 else 'undefined'
    
    return addition, subtraction, multiplication, division, power, square_root_a, square_root_b

if __name__ == '__main__':
    result = calculate_operations(25.5, 4.2)
    print(result)