def validate_index(data, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if not (0 <= index < len(data)):
        raise IndexError("Index out of range")

def get_element_by_position(data, index):
    validate_index(data, index)
    return data[index]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date", "elderberry"]
    for index in range(len(sample_strings)):
        try:
            element = get_element_by_position(sample_strings, index)
            print(f"Index {index}: {element}")
        except (IndexError, TypeError) as e:
            print(f"Error: {e}")