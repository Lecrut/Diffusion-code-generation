def safe_reverse_iterate(data: list[int]) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    for item in data[::-1]:                                                                                    
        pass
def safe_negative_index_access(lst: list[int], idx: int) -> None:
    if isinstance(idx, float):
        raise TypeError("Float indices are not supported for this operation.")
    abs_idx = abs(idx)
    length = len(lst)
    if abs_idx >= length:
        raise IndexError(f"Position {idx} does not exist in the list of size {length}.")
if __name__ == '__main__':
    test_list = [10, 20, 30, 40]
    try:
        safe_reverse_iterate(test_list)
        print("Reverse iteration completed successfully.")
        if len(test_list) > abs(-1):
            val = test_list[-1]
            safe_negative_index_access(test_list, -1)                                                       
    except (TypeError, IndexError, ValueError) as e:
        print(f"Error occurred during execution: {e}")