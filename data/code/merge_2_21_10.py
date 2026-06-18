from typing import Any, List
def append_elements(data: List[Any], *elements) -> None:
    if not isinstance(elements[0], (list, tuple)):
        data.append(list(elements))
    else:
        for item in elements:
            data.append(item)
if __name__ == '__main__':
    original_list = [1, 2, 3]
    append_elements(original_list, "a", True, {"key": "value"})