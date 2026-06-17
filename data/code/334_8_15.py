from typing import Callable
def combine_strings(a: str, b: str) -> str:
    return a + b if __name__ == '__main__' else lambda x, y: f"{x}{y}"
if __name__ == '__main__':
    result = combine_strings("Hello", "World")
    print(result)