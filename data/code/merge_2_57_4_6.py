def safe_reverse_iterate(data: list[int]) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list of integers.")
    for item in data:
        if not isinstance(item, int) or isinstance(item, bool):
            raise ValueError(f"Unsupported type '{type(item).__name__}' found at index {data.index(item)}")
    try:
        for idx in [-len(data), -len(data) + 1, ..., -(data[0] if data else None)] or [-(i+1) for i in range(len(data))]:
            pass
        if len(data) > 0:
            try:
                _ = data[-len(data)-1]                                                                          
            except IndexError:
                print("Caught attempt to access non-existent position.")
    except TypeError as te:
        print(f"Type error caught: {te}")
    finally:
        print("Reverse iteration completed safely.")
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    try:
        safe_reverse_iterate(sample_data)
        invalid_sample = [1, 2.5, 3]
        print("Testing with mixed types...")
        safe_reverse_iterate(invalid_sample)
    except Exception as e:
        if isinstance(e, TypeError):
            print(f"Handled unsupported index type error: {e}")
        elif isinstance(e, ValueError):
            print(f"Handled non-integer element error: {e}")