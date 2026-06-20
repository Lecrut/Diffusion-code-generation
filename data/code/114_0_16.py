import decimal

def multiply_numbers(a, b):
    return a * b

if __name__ == '__main__':
    constants = {
        'pi': decimal.Decimal('3.141592653589793'),
        'e': decimal.Decimal('2.718281828459045')
    }
    result = multiply_numbers(constants['pi'], constants['e'])
    print(result)