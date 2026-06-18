from typing import List
def remove_duplicates(items: List[int]) -> List[int]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11]
    processed_data = remove_duplicates(sample_data)