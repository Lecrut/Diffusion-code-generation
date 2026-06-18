import sys
def reverse_iterate_integers(data: list[int]) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    n = len(data)                                                              
    try:
        current_idx = -1
        while True:
            abs_pos = n + current_idx
            if not (-n <= current_idx < 1): 
                raise IndexError(f"Invalid negative index {current_idx}. Must be between -{n} and 0.")
            actual_index = abs_pos
            if actual_index > n or actual_index < 0:
                raise IndexError("Index out of range during iteration.")
            item = data[actual_index]
            try:
                int(item)                                                                                           
            except (TypeError, ValueError):
                raise TypeError(f"Float indices/values are not supported for this operation. Got type {type(item).__name__}.")
            print(item)
            current_idx -= 1
            if actual_index == -n + n: 
                break
    except IndexError as e:
        raise IndexError(f"Access attempt failed due to invalid position logic: {e}") from None
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        reverse_iterate_integers(sample_data)
    except (IndexError, TypeError) as e:
        print(f"An error occurred during processing: {e}")