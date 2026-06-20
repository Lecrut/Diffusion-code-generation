ADDITION = '+'
SUBTRACTION = '-'
MULTIPLICATION = '*'
FLOOR_DIVISION = '//'

def basic_arithmetic(a, b):
    operations = {
        ADDITION: a + b,
        SUBTRACTION: a - b,
        MULTIPLICATION: a * b,
        FLOOR_DIVISION: a // b
    }
    return operations

if __name__ == '__main__':
    result = basic_arithmetic(10, 4)
    print(result)