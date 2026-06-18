def count_elements(collection):
    try:
        if not hasattr(collection, "__iter__"):
            raise TypeError("Input must be iterable")
        counter = 0
        for _ in collection:
            counter += 1
        return counter
    except Exception as e:
        print(f"Error occurred during iteration: {e}")
        return None
if __name__ == '__main__':
    sample_data = [1, 2, "a", True]
    try:
        result = count_elements(sample_data)
        if result is not None:
            print(f"Total elements counted: {result}")
        invalid_input = 42
        try:
            count_invalid = count_elements(invalid_input)
        except TypeError as te:
            print(f"Caught expected error for non-iterable type: {te}")
    except Exception as e:
        print(f"Unexpected fatal error: {e}")