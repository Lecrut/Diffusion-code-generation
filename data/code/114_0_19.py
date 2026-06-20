def validate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")

def multiply_numbers(a, b):
    validate_number(a)
    validate_number(b)
    return a * b

if __name__ == '__main__':
    constants = {
        'pi': 3.141592653589793,
        'e': 2.718281828459045
    }
    result = multiply_numbers(constants['pi'], constants['e'])
    print(result)