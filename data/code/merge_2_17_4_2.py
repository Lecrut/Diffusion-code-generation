from typing import List, Tuple, Union
def search_optimized(data: Union[List[int], Tuple[int]], target: int) -> bool:
    if isinstance(data, list):
        return target in data
    elif isinstance(data, tuple):
        return target in data
    else:
        raise TypeError("Data must be a list or tuple.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (50, 60, 70)
    test_values = [20, 99, 60]
    for val in test_values:
        found_in_list = search_optimized(sample_list, val)
        found_in_tuple = search_optimized(sample_tuple, val)
        print(f"Searching {val}:")
        if found_in_list and not found_in_tuple:
            print("  Found only in list.")
        elif found_in_tuple and not found_in_list:
            print("  Found only in tuple.")
        else:
            print("  Not found in either or present in both (if applicable).")