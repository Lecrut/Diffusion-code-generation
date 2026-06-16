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
    sample_data: List[int] = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10, 3]
    cleaned_list: List[int] = remove_duplicates(sample_data)
    print(cleaned_list)