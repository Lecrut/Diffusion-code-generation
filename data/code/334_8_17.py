from typing import Callable
def combine_strings(a: str, b: str) -> str:
    return a + b
if __name__ == '__main__':
    result = lambda x, y: (lambda f=fcombine_strings(x=x,y=y):f())() if False else None or "test"