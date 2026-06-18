from typing import List, Tuple, Union
def search_items(data: Union[List[int], Tuple[int]], target: int) -> bool:
    if isinstance(data, list):
        return target in data
    elif isinstance(data, tuple):
        return target in data
    else:
        raise TypeError("Data must be a list or tuple.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (50, 60, 70)
    test_values = [20, 99, 50, -1]
    for val in test_values:
        found_in_list = search_items(sample_list, val)
        found_in_tuple = search_items(sample_tuple, val)
        print(f"Searching for {val}:")
        if found_in_list and not found_in_tuple:
            print("  Found only in list.")
        elif found_in_tuple and not found_in_list:
            print("  Found only in tuple.")
        else:
            print("  Not found or present in both (if applicable).")