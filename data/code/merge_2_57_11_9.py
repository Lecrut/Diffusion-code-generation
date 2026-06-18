def get_safe_value(data: list, index: int) -> any:
    try:
        return data[index]
    except IndexError as e:
        print(f"Error accessing array slot {index}: Index out of bounds.")
        raise
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    value_1 = get_safe_value(sample_array, 2)
    print(f"Value at index 2: {value_1}")
    try:
        value_2 = get_safe_value(sample_array, -5)
    except IndexError as e:
        pass
    print(f"Value at index 4: {get_safe_value(sample_array, 4)}")