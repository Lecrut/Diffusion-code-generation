from typing import Union

def signed_difference(a: int, b: int) -> int:
    return abs(a - b)

if __name__ == '__main__':
    result = signed_difference(10, 5)
    print(result)