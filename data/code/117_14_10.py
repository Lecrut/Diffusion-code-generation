from typing import Union

def signed_difference(a: int, b: int) -> int:
    return a - b if a >= b else b - a

if __name__ == '__main__':
    value1 = 30
    value2 = 20
    print(f"The signed difference between {value1} and {value2} is: {signed_difference(value1, value2)}")