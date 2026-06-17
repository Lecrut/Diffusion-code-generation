from typing import Callable, Tuple
def combine_strings(a: str, b: str) -> str:
    return f"{a}{b}"
if __name__ == '__main__':
    result = lambda x, y: (lambda z: print(z))(combine_strings("Hello", "World"))