from typing import Tuple

def signed_difference(a: int, b: int) -> int:
    return a - b if a >= b else -(b - a)

if __name__ == '__main__':
    sample_values = {
        'positive': (10, 5),
        'negative': (-5, 100),
        'zero_diff': (7, 7)
    }
    
    for key, values in sample_values.items():
        result = signed_difference(*values)
        print(f"Signed difference of {values}: {result}")