def safe_get_index(data: list, index: int) -> any:
    try:
        return data[index]
    except IndexError as e:
        print(f"Error: Index {index} is out of bounds for the array.")
        raise
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    try:
        value_valid = safe_get_index(sample_array, 2)
        print(f"Value at index 2: {value_valid}")
        value_invalid = safe_get_index(sample_array, -10)
    except IndexError as e:
        pass