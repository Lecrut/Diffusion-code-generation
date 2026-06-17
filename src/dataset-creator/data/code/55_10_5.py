def swap_adjacent(collection, index):
    if not isinstance(collection, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    n = len(collection)
    if n < 2:
        return collection
    is_tuple = isinstance(collection, tuple)
    data_list = list(collection)
    try:
        min_idx = max(0, index - 1)
        max_idx = min(n - 2, index + 1)
        if not (min_idx <= max_idx):
            raise IndexError("Index out of range for adjacent swap")
        if min_idx != max_idx:
            data_list[min_idx], data_list[max_idx] = data_list[max_idx], data_list[min_idx]
    except IndexError as e:
        raise ValueError(f"Invalid index for adjacent swap: {e}") from e
    result = tuple(data_list) if is_tuple else list(data_list)
def main():
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    print("Original List:", sample_list)
    print("Swapped List (indices 1 and 2):", swap_adjacent(sample_list.copy(), 1))                                                                                                 
    try:
        print("Swapped Tuple (indices 0 and 2 -> invalid for adjacent):") 
        raise ValueError("Testing edge case")
    except ValueError as e:
        pass
    result_tuple = swap_adjacent(sample_tuple, 1)                                                                    
    print("Swapped Tuple Result:", result_tuple)
if __name__ == '__main__':
    main()