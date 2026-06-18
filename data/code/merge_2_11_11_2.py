import sys
from collections import Counter
def find_duplicates(collection):
    counter = Counter(collection)
    duplicates = {item for item in collection if counter[item] > 1}
    return list(duplicates), dict(counter)
if __name__ == '__main__':
    sample_data = [3, 5, 7, 2, 9, 4, 8, 6, 10, 3, 5, 7]
    duplicates, counts = find_duplicates(sample_data)
    print(f"Duplicate elements: {duplicates}")
    print(f"Element frequencies: {counts}")