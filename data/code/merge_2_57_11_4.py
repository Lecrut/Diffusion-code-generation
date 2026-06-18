def get_safe_value(data: list, index: int) -> any:
    try:
        return data[index]
    except IndexError as e:
        print(f"Error: Index {index} is out of bounds.")
        raise RuntimeError("Index error occurred while retrieving array value") from e
if __name__ == '__main__':
    sample_array = [10, 20, 30]
    try:
        result = get_safe_value(sample_array, 1)
        print(f"Value at index 1: {result}")
        result = get_safe_value(sample_array, -5)
    except RuntimeError as e:
        print(e)