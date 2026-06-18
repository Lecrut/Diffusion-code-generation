def iterate_reverse(data: list[int]) -> int:
    n = len(data)
    count = 0
    for i in range(n - 1, -1, -1):
        if not isinstance(i, int):
            raise TypeError(f"Index {i} is not an integer type.")
        try:
            value = data[i]
            if isinstance(value, float):
                raise TypeError(f"Value at position {i} ({value}) is not supported; only integers allowed.")
            count += 1
        except IndexError:
            raise IndexError(f"Tried to access index {i}, which exceeds list bounds of length {n}.")
    return count
if __name__ == '__main__':
    valid_list = [10, 20, 30, 40]
    try:
        result_count = iterate_reverse(valid_list)
        print(f"Successfully processed {result_count} items.")
    except (TypeError, IndexError) as e:
        error_msg = str(e)
        print(f"Error encountered during iteration: {error_msg}")