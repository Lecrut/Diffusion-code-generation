def find_final_index(indices):
    try:
        if not isinstance(indices, list):
            raise TypeError("Input must be a list.")
        if not all(isinstance(i, int) for i in indices):
            raise ValueError("All elements in the list must be integers.")
        if len(indices) == 0:
            return -1
        return indices[-1]
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_indices = [10, 20, 30, 40, 50]
    final_index = find_final_index(sample_indices)
    print(final_index)

    invalid_input = "not a list"
    final_index_invalid = find_final_index(invalid_input)
    print(final_index_invalid)

    mixed_type_list = [1, 'two', 3]
    final_index_mixed = find_final_index(mixed_type_list)
    print(final_index_mixed)

    empty_list = []
    final_index_empty = find_final_index(empty_list)
    print(final_index_empty)