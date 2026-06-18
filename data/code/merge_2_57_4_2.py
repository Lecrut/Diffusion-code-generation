def safe_reverse_iterate(data: list[int]) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    for item in data:
        if not isinstance(item, int) or isinstance(item, bool):
            raise ValueError(f"List contains unsupported type {type(item).__name__}.")
    for idx, value in enumerate(reversed(data)):
        print(value)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        safe_reverse_iterate(sample_data)
    except (TypeError, ValueError) as e:
        print(f"Error encountered during iteration: {e}")