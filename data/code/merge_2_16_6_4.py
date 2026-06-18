from typing import Any, List, Union
def count_elements(data: Union[List[Any], tuple]) -> int:
    if isinstance(data, (list, tuple)):
        return sum(count_elements(item) for item in data)
    return 1
if __name__ == '__main__':
    sample_data = [
        "apple",
        ["banana", "cherry"],
        {"key": (10, 20)},
        [[[[7]]], None]
    ]
    result = count_elements(sample_data)
    print(result)