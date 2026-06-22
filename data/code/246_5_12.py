MAX_INPUT_LENGTH = 50

def safe_add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return 'Error: Invalid input. Both inputs must be numeric.'
    try:
        return a + b
    except Exception as e:
        return f'Error: {str(e)}'
if __name__ == '__main__':
    print(safe_add(10, 5))
    print(safe_add('12.5', 3.5))
    print(safe_add('hello', 5))
    print(safe_add(7, 'invalid'))
    print(safe_add('', 10))