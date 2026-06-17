from typing import Tuple
def multiply(a: int, b: int) -> Tuple[int]:
    return (a * b,)
if __name__ == '__main__':
    result = multiply(5, 3)[0]
    print(result)