from typing import List, Tuple
def filter_positive_numbers(data: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [entry for entry in data if entry[0] >= 0 and entry[1] > 0]
if __name__ == '__main__':
    sample_data = [(5, -2), (-3, 4), (7, 8), (0, 9)]
    cleaned_data: List[Tuple[int, int]] = filter_positive_numbers(sample_data)
    print(cleaned_data)