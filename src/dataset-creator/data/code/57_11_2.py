def get_safe_value(data: list, index: int) -> any:
    try:
        return data[index]
    except IndexError as e:
        print(f"Error accessing array slot {index}: Index out of bounds.")
        raise Exception("Index error occurred while retrieving value.", exc_info=True)
if __name__ == '__main__':
    sample_array = [10, 20, 30]
    try:
        result = get_safe_value(sample_array, 1)
        print(f"Value at index 1 is {result}")
    except Exception as e:
        pass
    try:
        result = get_safe_value(sample_array, -5)
    except Exception as e:
        print("Handled exception for invalid index.")