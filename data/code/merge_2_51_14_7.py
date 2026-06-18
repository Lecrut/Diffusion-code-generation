def get_first_element(collection):
    if collection is None:
        raise ValueError("Input cannot be null.")
    try:
        return next(iter(collection))
    except StopIteration:
        raise IndexError("Collection is empty.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first_element(sample_list)
    print(f"First element: {result}")
    try:
        get_first_element(None)
    except ValueError as e:
        print(f"Caught expected error for null input: {e}")
    sample_empty = []
    try:
        get_first_element(sample_empty)
    except IndexError as e:
        print(f"Caught expected error for empty collection: {e}")