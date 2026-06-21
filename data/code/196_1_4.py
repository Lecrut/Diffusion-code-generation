from typing import List

class ListMerger:
    @staticmethod
    def merge(list1: List[int], list2: List[int]) -> List[int]:
        return [item for sublist in (list1, list2) for item in sublist]

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    merged_result = ListMerger.merge(sample_list_a, sample_list_b)
    print(merged_result)