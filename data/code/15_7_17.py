from typing import List, TypeVar, Optional

T = TypeVar('T')

ELEMENT_INDEX_MAP = {
    "second_last": -2,
}

def get_second_last_element(data: List[T]) -> Optional[T]:
    if len(data) < 2:
        return None
    index = ELEMENT_INDEX_MAP["second_last"]
    return data[index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20],
        [1],
        []
    ]
    for item in test_cases:
        output = get_second_last_element(item)
        print(output)