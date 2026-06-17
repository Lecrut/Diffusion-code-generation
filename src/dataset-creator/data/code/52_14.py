from typing import Any, Iterable
def get_last_item(sequence: Iterable[Any]) -> Any | None:
    try:
        return next(reversed(sequence))
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 'end', True]
    result = get_last_item(sample_sequence)
    print(result)