from typing import Dict
operations: Dict[str, callable] = {'add': lambda x, y: x + y, 'subtract': lambda x, y: x - y, 'multiply': lambda x, y: x * y, 'divide': lambda x, y: x / y if y != 0 else float('inf')}

def perform_operation(operation: str, a: int, b: int) -> float:
    return operations.get(operation, lambda _, __: None)(a, b)
if __name__ == '__main__':
    print(perform_operation('add', 5, 3))
    print(perform_operation('subtract', 10, 4))
    print(perform_operation('multiply', 7, 2))
    print(perform_operation('divide', 9, 3))
    print(perform_operation('divide', 9, 0))