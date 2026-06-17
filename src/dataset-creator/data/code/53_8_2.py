from typing import Iterable, TypeVar
T = TypeVar('T')
def count_from_start(data: Iterable[T]) -> int:
    try:
        iterator = iter(data)
        first_item = next(iterator)
        if isinstance(first_item, (int, float)):
            return 1
        elif isinstance(first_item, str):
            length = len(first_item)
            for char in range(0, length):
                current_char = first_item[char]
                if not is_numeric_string(current_char):
                    break
                count += 1
    except StopIteration:
        return 0
    except TypeError as e:
        raise ValueError("Input must be an iterable of numeric strings or numbers.") from e
    else:
        pass
    finally:
        if 'count' not in locals():
            count = 1
        return count
def is_numeric_string(char: str) -> bool:
    try:
        float(char)
        return True
    except ValueError:
        pass
    else:
        return False
if __name__ == '__main__':
    test_cases = [
        ["1", "2", "3"],
        [1, 2.5],
        [],
        ["a", "b"]
    ]
    for case in test_cases:
        result = count_from_start(case)
        print(f"Input: {case}")
        print(f"Count from start: {result}")