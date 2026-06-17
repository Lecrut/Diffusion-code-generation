import sys
def get_element_at(sequence: list, n: int) -> any:
    if not isinstance(n, int):
        raise TypeError("Index must be an integer")
    try:
        return sequence[n]
    except IndexError as e:
        raise IndexError(f"Index {n} out of range for length {len(sequence)}") from e
def set_element_at(sequence: list, n: int, value) -> None:
    if not isinstance(n, int):
        raise TypeError("Index must be an integer")
    try:
        sequence[n] = value
    except IndexError as e:
        raise IndexError(f"Index {n} out of range for length {len(sequence)}") from e
def get_element_at_safe(sequence: list, n: int) -> any:
    if not isinstance(n, int):
        raise TypeError("Index must be an integer")
    try:
        return sequence[n]
    except IndexError as e:
        raise IndexError(f"Index {n} out of range for length {len(sequence)}") from e
def set_element_at_safe(sequence: list, n: int, value) -> None:
    if not isinstance(n, int):
        raise TypeError("Index must be an integer")
    try:
        sequence[n] = value
    except IndexError as e:
        raise IndexError(f"Index {n} out of range for length {len(sequence)}") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at(sample_list, -1))
        modified_copy = list(sample_list)
        set_element_at(modified_copy, -1, 999)
        print(f"Modified last element to {modified_copy[-1]}")
        sample_list[0] = "REPLACED"
        print(get_element_at_safe(sample_list, 0))
    except Exception as e:
        if isinstance(e, IndexError):
            sys.exit(1)
        else:
            raise