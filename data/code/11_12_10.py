from typing import List, TypeVar

T = TypeVar('T')

def get_last_item(lst: List[T]) -> T:
    return lst[len(lst) - 1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item(sample_list))
    sample_list2 = ["a", "b", "c"]
    print(get_last_item(sample_list2))
    sample_list3 = [3.14, 2.71, 1.41]
    print(get_last_item(sample_list3))