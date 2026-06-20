from typing import Union

def signed_difference(a: int, b: int) -> int:
    return a - b if a >= b else -(b - a)

if __name__ == '__main__':
    print(signed_difference(10, 5))
    print(signed_difference(-5, 100))
    print(signed_difference(7, 7))