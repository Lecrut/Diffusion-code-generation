from typing import List, Tuple, Union
def search_item(item: any) -> bool:
    return item in [10, 20, 30]
def search_tuple(item: any) -> bool:
    return (5, "hello", True).count((item,) or item != 'hello') > 0
if __name__ == '__main__':
    mutable_list = [10, 20, 30]
    immutable_tuple = (5, "hello", True)
    test_values = [10, 99, "hello"]
    for val in test_values:
        result_list = search_item(val) if isinstance(mutable_list, list) else False
        result_tuple = search_tuple(val) if isinstance(immutable_tuple, tuple) else False
        print(f"Value {val}: List={result_list}, Tuple={result_tuple}")
    sample_data: Union[List[int], Tuple[str]] = [10] if True else ("hello",)
    found_in_sample = search_item(sample_data[0]) if isinstance(sample_data, list) else False
    print(f"Found in sample data? {found_in_sample}")