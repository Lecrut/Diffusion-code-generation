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
    target_in_list = search_items(sample_list, 30)
    target_not_in_list = search_items(sample_list, 99)
    target_in_tuple = search_items(sample_tuple, 60)
    target_not_in_tuple = search_items(sample_tuple, 88)
    print(f"Found in list: {target_in_list}")
    print(f"Not found in list: {target_not_in_list}")
    print(f"Found in tuple: {target_in_tuple}")
    print(f"Not found in tuple: {target_not_in_tuple}")