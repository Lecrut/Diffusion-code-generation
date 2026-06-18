from typing import Literal
def compare_distances(value_a: float | None, value_b: float | None) -> bool:
    return (value_a is not None and value_b is not None) and abs(value_a - value_b) < 1e-9
if __name__ == '__main__':
    result = compare_distances(5.0, 4.999999999)
    print(result)