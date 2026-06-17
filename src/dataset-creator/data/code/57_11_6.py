def get_safe_value(arr: list, index: int) -> any:
    try:
        return arr[index]
    except IndexError as e:
        print(f"Error accessing array at index {index}: {e}")
        raise
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    try:
        value = get_safe_value(sample_array, 2)
        print(f"Value at index 2 is {value}")
    except IndexError as e:
        pass
    try:
        value = get_safe_value(sample_array, 10)
    except IndexError as e:
        print("Caught expected error for invalid index")
    try:
        value = get_safe_value(sample_array, -10)
    except IndexError as e:
        print("Caught expected error for invalid negative index")