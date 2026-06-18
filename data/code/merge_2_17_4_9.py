from typing import List, Tuple, Union
def search_items(data: Union[List[int], Tuple[int]], target: int) -> bool:
    if isinstance(data, list):
        return target in data
    elif isinstance(data, tuple):
        return target in data
    else:
        raise TypeError("Data must be a list or tuple.")
if __name__ == '__main__':
    mutable_data = [10, 25, 30, 45]
    immutable_data = (10, 20, 30, 60)
    target_value = 30
    result_mutable = search_items(mutable_data, target_value)
    result_immutable = search_items(immutable_data, target_value)
    print(f"Found in list: {result_mutable}")
    print(f"Found in tuple: {result_immutable}")