def safe_reverse_iterate(data: list[int]) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    for i in range(-len(data), 0):
        try:
            value = data[i]
        except IndexError as exc_info:
            print(f"IndexError caught at position {i}: {exc_info}")
            continue
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("All elements must be integers; floats are unsupported.")
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    try:
        safe_reverse_iterate(sample_data)
    except (TypeError, IndexError) as e:
        print(f"An error occurred during iteration: {e}")