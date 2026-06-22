ADD_KEY = 'addition'
SUB_KEY = 'subtraction'
MUL_KEY = 'multiplication'
DIV_KEY = 'division'

def calculate_operations(a: int, b: int) -> dict:
    operations = {ADD_KEY: a + b, SUB_KEY: a - b, MUL_KEY: a * b, DIV_KEY: a / b if b != 0 else None}
    return operations
if __name__ == '__main__':
    result = calculate_operations(10, 5)
    print(result)