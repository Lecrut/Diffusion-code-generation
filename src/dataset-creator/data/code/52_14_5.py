from typing import Any, Sequence
def get_last_item(sequence: Sequence[Any]) -> Any:
    return sequence[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)