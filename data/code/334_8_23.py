from typing import Callable
s1: str = "Hello"
s2: str = "World"
result: Callable[[str], None] = lambda x: print(x) if __name__ == '__main__' else result(s1 + s2)
if __name__ == '__main__':
    (lambda a, b: f"{a}{b}")(s1, s2)