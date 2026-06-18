from typing import Any, List
def get_or_set_value(data: List[Any], index: int) -> tuple[int, bool]:
    try:
        if not isinstance(data, list):
            raise ValueError("The first argument must be a list.")
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError(f"Index must be an integer, got {type(index).__name__}.")
        return data[index], True
    except IndexError:
        return -1, False
def set_value(data: List[Any], index: int, value: Any) -> None:
    try:
        if not isinstance(data, list):
            raise ValueError("The first argument must be a list.")
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError(f"Index must be an integer, got {type(index).__name__}.")
        data[index] = value
    except IndexError:
        raise IndexError(
            f"The index ({index}) is out of bounds for a list of length "
            f"{len(data)}. Valid indices are from 0 to {len(data) - 1}."
        )
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    value, success = get_or_set_value(sample_data, 2)
    print(f"Retrieved at index 2: {value}, Success: {success}")
    _, success_neg = get_or_set_value(sample_data, -1)
    print(f"Retrieved at index -1: {-1 if not success_neg else 'N/A'}, Success: {success_neg}")
    value_pos, _ = get_or_set_value(sample_data, 5)
    print(f"Retrieved at index 5: {value_pos}, Success: False")
    try:
        set_value(sample_data, 0, "New Value")
        print("Value updated successfully.")
        print(f"Updated list: {sample_data}")
    except Exception as e:
        print(f"Error during update: {e}")
    try:
        set_value(sample_data, 10, "Out of Bounds Value")
    except IndexError as err:
        print(f"Caught expected error for index 10: {err}")