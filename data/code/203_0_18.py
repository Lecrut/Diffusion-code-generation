import sys

MAX_COMPARE_VALUE = 1e308

def compare_numbers(a, b):
    if abs(a) > MAX_COMPARE_VALUE or abs(b) > MAX_COMPARE_VALUE:
        return "Error: One or both numbers are too large."
    
    if a == b:
        return 'Equal'
    elif a > b:
        return 'Greater'
    else:
        return 'Lesser'

if __name__ == '__main__':
    num1 = 123456789.0
    num2 = 987654321.0
    result = compare_numbers(num1, num2)
    print(result)