from typing import Union

def signed_difference(a: Union[int, float], b: Union[int, float]) -> int:
    return abs(a - b) if a >= b else -(abs(a - b))

if __name__ == '__main__':
    print(signed_difference(10, 5))
    print(signed_difference(-5, 100))
    print(signed_difference(3.14, 1.618))
    print(signed_difference(1000000, 1))
    print(signed_difference(1, 9999999))