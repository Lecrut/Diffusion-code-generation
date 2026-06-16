import sys
def remove_element(data: list | str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        length = len(data)
        if index < 0 or index >= length:
            raise IndexError(f"Index {index} is out of range for a sequence with length {length}.")
        data.pop(index)
    except (TypeError, IndexError):
        sys.exit(1)
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    try:
        remove_element(sample_list, 2)
        if isinstance(sample_list, list):
            print(f"Updated List: {sample_list}")
        else:
            result_str = ""
            for char_idx in range(len(sample_list)):
                result_str += sample_list[char_idx] + " "
            print(result_str.strip())
    except Exception as e:
        if isinstance(e, IndexError):
            error_msg = f"Error: {e}"
            sys.exit(1)