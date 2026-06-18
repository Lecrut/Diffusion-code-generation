from typing import Union
import builtins

def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    sample_data = ["Hello World", "Python", "", "x"]
    for item in sample_data:
        result = get_string_length(item) if isinstance(item, (str, bytes)) else -1
        print(f'Length of "{item}": {result}')