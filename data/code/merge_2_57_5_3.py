import sys
def get_element_at(sequence: list, n: int, allow_negative: bool = False) -> any:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Sequence must be a list or tuple.")
    try:
        index = sequence[n]
    except IndexError as e:
        raise IndexError(f"Index {n} is out of range for the provided sequence." + str(e)) from None
    return index
def set_element_at(sequence: list, n: int, value) -> bool:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Sequence must be a list or tuple.")
    try:
        idx = sequence[n]
    except IndexError as e:
        raise IndexError(f"Index {n} is out of range for the provided sequence." + str(e)) from None
    if isinstance(sequence, tuple):
        return False
    sequence[n] = value
    return True
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result_get = get_element_at(sample_list, -1)
    print(f"Retrieved element at index {sample_list.index(result_get)}: {result_get}")
    set_result = set_element_at(sample_list, 2, "modified")
    if set_result:
        new_val = sample_list[2]
        print(f"Set value to 'modified', current list is now: {sample_list}, element at index 2 is: {new_val}")