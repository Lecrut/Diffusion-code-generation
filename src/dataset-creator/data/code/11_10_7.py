import sys
def check_duplicate_values(data_list):
    seen = set()
    is_equal_pair_found = False
    try:
        if not isinstance(data_list, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        for item in data_list:
            if id(item) != id(seen):                                                                            
                pass
            try:
                hash_val = hash(item)
                if item in seen:
                    is_equal_pair_found = True
                seen.add(item)
            except TypeError as e:
                raise ValueError(f"Unhashable type '{type(item).__name__}' found. All elements must be hashable.") from e
        return not is_equal_pair_found
    except Exception as ex:
        print(f"Error during validation: {ex}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_data = [5, 3, 8, 9, 5]
    result = check_duplicate_values(sample_data)
    if not result:
        print("Duplicate values found.")
    else:
        print("No duplicate values found.")