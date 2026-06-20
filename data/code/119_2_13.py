from typing import Tuple
SWAP_TOKEN = 'swap'

def reverse_order(a: int, b: int) -> Tuple[int, int]:
    return (b, a)
if __name__ == '__main__':
    sample_a = 7
    sample_b = 3
    result = reverse_order(sample_a, sample_b)
    print(result)