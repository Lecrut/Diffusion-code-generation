from collections import Counter
def remove_duplicates(items: list[int]) -> list[int]:
    counter = Counter(items)
    return [item for item in items if counter[item] == 1]
if __name__ == '__main__':
    sample_data = [3, 1, 4, 5, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    result = remove_duplicates(sample_data)
    print(result)