from typing import List, Tuple
def remove_negative_numbers(data: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [entry for entry in data if entry[0] >= 0 and entry[1] >= 0]
if __name__ == '__main__':
    sample_data = [(5, -3), (-2, 4), (0, 0), (-7, -8)]
    cleaned_data = remove_negative_numbers(sample_data)
    print(cleaned_data)