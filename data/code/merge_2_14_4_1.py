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
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    cleaned_data = remove_duplicates(sample_data)
    print(cleaned_data)