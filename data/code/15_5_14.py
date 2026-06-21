from typing import List, Any

INDEX_MAP: dict[str, int] = {
    "last": -1,
    "second_to_last": -2,
    "first": 0
}

def get_second_to_last(values: list[Any]) -> Any:
    return values[INDEX_MAP["second_to_last"]]

if __name__ == '__main__':
    test_data: List[int] = [5, 10, 15, 20, 25]
    print(get_second_to_last(test_data))