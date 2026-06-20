from typing import Tuple

def reverse_order(a: int, b: int) -> Tuple[int, int]:
    return (b, a)

if __name__ == '__main__':
    num_a = 15
    num_b = 20
    result = reverse_order(num_a, num_b)
    print(result)