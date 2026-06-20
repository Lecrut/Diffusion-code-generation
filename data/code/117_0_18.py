def validate_input(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be integers or floats.")

def calculate_difference(num1, num2):
    try:
        validate_input(num1, num2)
        return num1 - num2
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    difference = calculate_difference(15, 7)
    print(difference)