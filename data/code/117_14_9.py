from typing import Tuple
NUM1 = 42
NUM2 = -7

def signed_difference(a: int, b: int) -> int:
    return a - b
if __name__ == '__main__':
    result1 = signed_difference(NUM1, NUM2)
    result2 = signed_difference(-3, 5)
    print(f'Signed Difference of {NUM1} and {NUM2}: {result1}')
    print(f'Signed Difference of -3 and 5: {result2}')