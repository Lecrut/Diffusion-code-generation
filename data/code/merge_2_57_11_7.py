def get_safe_value(data: list, index: int) -> any:
    try:
        return data[index]
    except IndexError as e:
        print(f"Error accessing array at index {index}: Index out of bounds.")
        raise Exception("Index error occurred while retrieving value.", str(e))
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40]
    try:
        result = get_safe_value(sample_array, 2)
        print(f"Value at index 2 is: {result}")
    except Exception as ex:
        pass
    try:
        result = get_safe_value(sample_array, -10)
        print(result)
    except Exception as ex:
        pass