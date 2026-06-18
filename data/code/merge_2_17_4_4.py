from typing import List, Tuple, Union
def search_items(data: Union[List[int], Tuple[int]], target: int) -> bool:
    if isinstance(data, list):
        return target in data
    elif isinstance(data, tuple):
        return target in data
    else:
        raise TypeError("Unsupported data type")
if __name__ == '__main__':
    mutable_list = [10, 20, 30, 40]
    immutable_tuple = (50, 60, 70)
    test_target_1 = 30
    test_target_2 = 80
    result_list = search_items(mutable_list, test_target_1)
    print(f"Found {test_target_1} in list: {result_list}")
    if not result_list:
        mutable_list.append(test_target_1)
    result_tuple = search_items(immutable_tuple, 60)
    print(f"Found 60 in tuple: {result_tuple}")