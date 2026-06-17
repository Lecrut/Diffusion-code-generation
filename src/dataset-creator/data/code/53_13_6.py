import sys
def count_elements(collection):
    try:
        if not hasattr(collection, "__iter__"):
            raise TypeError("Input must be iterable")
        counter = 0
        for _ in collection:
            counter += 1
        return counter
    except Exception as e:
        print(f"Error processing input: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_data = [1, 2, 3, "a", "b"]
    try:
        result = count_elements(sample_data)
        print(f"Total elements counted: {result}")
        test_input = (42,)
        if not hasattr(test_input, "__iter__"):
            raise TypeError("Test failure for non-iterable")
    except Exception as e:
        print(f"Exception occurred during execution: {e}", file=sys.stderr)