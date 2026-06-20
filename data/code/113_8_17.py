ZERO = 0

def subtract(a, b):
    return a - b
if __name__ == '__main__':
    result1 = subtract(10, 5)
    print(f'10 - 5 = {result1}')
    result2 = subtract(5, 10)
    print(f'5 - 10 = {result2}')
    result3 = subtract(ZERO, 5)
    print(f'{ZERO} - 5 = {result3}')
    result4 = subtract(5, ZERO)
    print(f'5 - {ZERO} = {result4}')
    result5 = subtract(-10, 5)
    print(f'-10 - 5 = {result5}')
    result6 = subtract(5, -10)
    print(f'5 - (-10) = {result6}')
    result7 = subtract(-10, -5)
    print(f'-10 - (-5) = {result7}')
    result8 = subtract(ZERO, ZERO)
    print(f'{ZERO} - {ZERO} = {result8}')