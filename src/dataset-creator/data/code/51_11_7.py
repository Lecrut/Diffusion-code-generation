def get_first_item(iterable):
    if not iterable:
        raise ValueError("Input iterable cannot be empty.")
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("No items found in the input iterable.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    if not isinstance(sample_list, (list, tuple)):
        print("Error: Input must be a list or tuple.")
    else:
        try:
            first_item = get_first_item(sample_list)
            print(f"The initial item is: {first_item}")
        except ValueError as e:
            print(f"Validation error: {e}")