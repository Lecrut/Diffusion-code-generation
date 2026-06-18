from typing import Any
def get_first_element(sequence: list[Any]) -> Any:
    return next(iter(sequence)) if sequence else None
if __name__ == '__main__':
    sample_sequence = [10, 20, 30]
    result = get_first_element(sample_sequence)
    print(result)