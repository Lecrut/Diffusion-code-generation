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
    sample_data = [1, 2, 3, "a", "b"]
    try:
        result = count_elements(sample_data)
        if result is not None:
            print(f"Count of elements in {sample_data}: {result}")
        invalid_input = 42
        result_invalid = count_elements(invalid_input)
        if result_invalid is None:
            print("Handled non-iterable input correctly.")
    except Exception as e:
        print(f"Unexpected error in main block: {e}")