from typing import Tuple

def signed_difference(a: int, b: int) -> int:
    return abs(a - b)

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 5
    }
    result = signed_difference(sample_values['a'], sample_values['b'])
    print(result)