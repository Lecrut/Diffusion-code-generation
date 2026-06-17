def get_first_element(collection):
    if collection is None:
        raise ValueError("Input cannot be null.")
    try:
        return list(collection)[0]
    except IndexError as e:
        raise RuntimeError(f"Collection is empty. Error details: {e}") from e
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    result = get_first_element(sample_list)
    print(result)
    try:
        get_first_element([])
    except RuntimeError as error:
        print(f"Caught expected error for empty list: {error}")
    try:
        get_first_element(None)
    except ValueError as error:
        print(f"Caught expected error for null input: {error}")