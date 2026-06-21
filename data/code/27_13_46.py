from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not a == b
if __name__ == '__main__':
    sample_values = [(1, 2), ('hello', 'world'), ([1, 2, 3], [1, 2, 3]), (3.0, 3), (None, None)]
    comparison_dict = {'numeric': (5, 10), 'string': ('test', 'sample'), 'list': ([1, 2], [2, 1]), 'float': (3.14, 3.14159), 'none': (None, None)}
    for a, b in sample_values:
        print(are_different(a, b))
    for key, (a, b) in comparison_dict.items():
        print(f'{key.capitalize()}: {are_different(a, b)}')