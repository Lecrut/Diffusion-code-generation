from typing import Union

operations = {
    'add': lambda a, b: a + b,
    'subtract': lambda a, b: a - b
}

def calculate(operation: str, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return operations[operation](a, b)

if __name__ == '__main__':
    result_add = calculate('add', 5, 3)
    result_sub = calculate('subtract', 10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")