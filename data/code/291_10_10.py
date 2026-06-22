from typing import Union

def compare_lengths(length1: float, length2: float) -> Union[float, None]:
    if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
        return None
    return max(length1, length2)

if __name__ == '__main__':
    print(compare_lengths(5.0, 3.0))
    print(compare_lengths(7.5, 7.5))
    print(compare_lengths('a', 3.0))