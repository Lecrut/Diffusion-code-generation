from typing import List

def contains_item(target: int, data_list: List[int]) -> bool:
    return target in set(data_list)
if __name__ == '__main__':
    sample_data = [i for i in range(1000000)]
    print(contains_item(500000, sample_data))
    print(contains_item(1000001, sample_data))