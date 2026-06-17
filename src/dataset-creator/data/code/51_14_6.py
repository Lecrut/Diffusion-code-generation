def get_first_element(data):
    if data is None:
        raise ValueError("Input cannot be null.")
    try:
        return list(data)[0] if isinstance(data, (list, tuple)) else next(iter(data), None)
    except TypeError as e:
        raise RuntimeError(f"Invalid collection type provided. {e}")
if __name__ == '__main__':
    samples = [None, [], "valid_list", 12345]
    for sample in samples:
        try:
            result = get_first_element(sample)
            print(f"Input: {sample} -> Output: {result}")
        except Exception as e:
            print(f"Error processing input {sample}: {e}")