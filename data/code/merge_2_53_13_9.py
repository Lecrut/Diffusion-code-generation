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
        print(f"Error occurred during iteration: {e}")
        sys.exit(1)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        result = count_elements(sample_list)
        print(f"Count of elements in collection: {result}")
        test_input = "not iterable"
        try:
            _ = count_elements(test_input)
        except TypeError as te:
            print(f"Caught expected error for non-iterable type: {te}")
    except Exception as e:
        sys.exit(1)