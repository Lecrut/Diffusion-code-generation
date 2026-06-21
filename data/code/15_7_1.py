from typing import List, Any, Optional

def get_second_last_element(items: List[Any]) -> Optional[Any]:
    if len(items) < 2:
        return None
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_last_element(sample_list)
    print(result)
    empty_list: List[int] = []
    result_empty = get_second_last_element(empty_list)
    print(result_empty)
    single_item = [42]
    result_single = get_second_last_element(single_item)
    print(result_single)