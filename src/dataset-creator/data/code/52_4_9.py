from typing import Any, Sequence
def get_last_element(data: Sequence[Any]) -> Any:
    return data[-1] if len(data) > 0 else None
if __name__ == '__main__':
    sample_list = [10, 'hello', True, 3.14]
    result = get_last_element(sample_list)
    print(result)