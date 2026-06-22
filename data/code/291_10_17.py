from typing import Union

def compare_lengths(length1: float, length2: float) -> Union[float, None]:
    if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
        return None
    return max(length1, length2)

if __name__ == '__main__':
    print(compare_lengths(5.7, 3.2))
    print(compare_lengths(4.8, 4.8))
    print(compare_lengths('a', 3.2))