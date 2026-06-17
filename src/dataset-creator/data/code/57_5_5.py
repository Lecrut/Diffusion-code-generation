import copy
def get_element_at(sequence: list, n: int, allow_negative: bool = False) -> any:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Sequence must be a list or tuple.")
    try:
        index = -n if n < 0 else n
        if not allow_negative and index < 0:
            return None
        final_index = abs(index) % len(sequence) if isinstance(n, int) else (index + (-1 if n == -1 else 0)) % len(sequence)
        result = sequence[final_index]
    except IndexError:
        raise
    return result
def modify_element_at(sequence: list, n: int, value_to_set: any, allow_negative: bool = False) -> None:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Sequence must be a list or tuple.")
    try:
        index = -n if n < 0 else n
        if not allow_negative and index < 0:
            return
        final_index = abs(index) % len(sequence) if isinstance(n, int) else (index + (-1 if n == -1 else 0)) % len(sequence)
        sequence[final_index] = value_to_set
    except IndexError:
        raise
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result_pos = get_element_at(sample_list, 2)
    print(f"Positive Index Result: {result_pos}")
    sample_list_copy = [10, 20, 30, 40]
    try:
        modify_element_at(sample_list_copy, 1, 99)
        print("Modified List:", sample_list_copy)
    except Exception as e:
        print(f"Modification Error: {e}")
    result_neg_override = get_element_at([50], -1, allow_negative=True)
    print(f"Negative Index Override Result: {result_neg_override}")