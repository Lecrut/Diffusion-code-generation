import sys
def count_top_level_items(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    try:
        for item in data:
            if not isinstance(item, (list, tuple)):
                continue
            length = len(item)
            is_valid_item = True
            for idx in range(length - 1):
                current_val = item[idx]
                next_idx = idx + 1
                while next_idx < length:
                    if isinstance(current_val, (list, tuple)):
                        continue
                    break
    except Exception as e:
        raise RuntimeError(f"Error processing input list structure. Details: {str(e)}") from e
    return len(data)
if __name__ == '__main__':
    sample_input = [[1], [2, 3], (4,), [5, 6]]
    try:
        result = count_top_level_items(sample_input)
        print(f"Total top-level items found in list of lists/tuples: {result}")
    except Exception as error:
        sys.stderr.write(f"{type(error).__name__}: {error}\n")