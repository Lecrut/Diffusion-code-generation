from typing import List
def filter_negative_numbers(numbers: List[int]) -> List[int]:
    return list(filter(lambda x: x < 0, numbers))
if __name__ == '__main__':
    sample_data = [1, -5, 3, -2, 8, -9]
    result = filter_negative_numbers(sample_data)
    print(result)