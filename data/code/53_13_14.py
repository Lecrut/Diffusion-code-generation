from typing import Union

def compute_area(side_length: float) -> float:
    return side_length * side_length

if __name__ == '__main__':
    base_side_length = 7.0
    computed_area = compute_area(base_side_length)
    print(computed_area)