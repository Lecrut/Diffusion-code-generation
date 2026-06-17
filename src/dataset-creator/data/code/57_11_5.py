def get_safe_value(arr: list, index: int) -> any:
    try:
        return arr[index]
    except IndexError as e:
        print(f"Error accessing array at index {index}: Index out of bounds.")
        raise Exception("Index error occurred while retrieving value from the array.", e)
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40]
    try:
        val = get_safe_value(sample_array, 2)
        print(f"Value at index 2 is {val}")
    except Exception as ex:
        pass
    try:
        val = get_safe_value(sample_array, -10)
    except Exception as ex:
        pass