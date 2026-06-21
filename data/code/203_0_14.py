def compare_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    if a > b:
        return 'Greater'
    elif a < b:
        return 'Lesser'
    else:
        return 'Equal'

if __name__ == '__main__':
    num1 = 3.14159
    num2 = 2.71828
    result = compare_numbers(num1, num2)
    print(result)