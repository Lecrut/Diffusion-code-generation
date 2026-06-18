def count_from_start(collection):
    try:
        if not hasattr(collection, "__iter__"):
            raise TypeError("Input must be iterable")
        counter = 0
        for item in collection:
            counter += 1
        return counter
    except Exception as e:
        print(f"Error occurred during iteration: {e}")
        return None
if __name__ == '__main__':
    sample_data = [1, 2, "three", True]
    try:
        result = count_from_start(sample_data)
        if result is not None:
            print(f"Count from start: {result}")
    except Exception as e:
        print(f"Fatal error in main block: {e}")
    try:
        invalid_input = "Not a list or tuple"
        result_invalid = count_from_start(invalid_input)
        if result_invalid is None:
            print("Handled non-iterable type correctly")
    except Exception as e:
        print(f"Unexpected error with invalid input: {e}")