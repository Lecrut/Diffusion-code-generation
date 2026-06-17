import sys
def get_array_value(arr: list, index: int) -> any:
    if not isinstance(arr, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        return arr[index]
    except IndexError as e:
        print(f"Error: Index out of bounds. Provided index was {index}, length is {len(arr)}.")
        sys.exit(1)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    try:
        value = get_array_value(sample_data, 2)
        print(f"Value at index 2 is {value}")
    except Exception as e:
        print(f"Unexpected error during test: {e}")
    try:
        value = get_array_value(sample_data, 5)
    except SystemExit:
        pass