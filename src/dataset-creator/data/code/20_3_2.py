from typing import List
def filter_negatives(numbers: List[int]) -> List[int]:
    return list(filter(lambda x: x < 0, numbers))
if __name__ == '__main__':
    sample_data = [1, -2, 3, -4, 5, -6]
    result = filter_negatives(sample_data)
    print(result)