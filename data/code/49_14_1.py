from typing import Union

def lengths_equal_within_threshold(
    len_a: int,
    len_b: int,
    threshold: Union[int, float] = 0
) -> bool:
    return abs(len_a - len_b) <= threshold

if __name__ == '__main__':
    result = lengths_equal_within_threshold(10, 12, 2)
    print(result)