def set_value(arr: list[int], index: int, value) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    elif len(arr) == 0 or (index < 0 or index >= len(arr)):
        raise IndexError(f"Array is empty. Index {index} out of bounds for array with length {len(arr)}.")
    arr[index] = value
def get_value(arr: list[int], index: int):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    elif len(arr) == 0 or (index < 0 or index >= len(arr)):
        raise IndexError(f"Array is empty. Index {index} out of bounds for array with length {len(arr)}.")
    return arr[index]
if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5]
    try:
        set_value(sample_array, 0, "Hello")
        retrieved_item = get_value(sample_array, 0)
        print(f"Retrieved item at index 0: {retrieved_item}")
        invalid_index = len(sample_array) + 1
        try:
            set_value(sample_array, invalid_index, "Error")
        except IndexError as e:
            print(f"Caught expected error during set operation: {e}")
    except Exception as ex:
        print(f"Unexpected exception occurred: {ex}")