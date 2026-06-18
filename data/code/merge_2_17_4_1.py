from typing import List, Tuple, Union
def search_items(data: Union[List[int], Tuple[int]], target: int) -> bool:
    if isinstance(data, list):
        return target in data
    elif isinstance(data, tuple):
        return target in data
    else:
        raise TypeError("Unsupported sequence type")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (50, 60, 70)
    target_val = 30
    if search_items(sample_list, target_val):
        print(f"Found {target_val} in list")
    found_in_tuple = search_items(sample_tuple, target_val)
    not_found_result = search_items(sample_list, 99)