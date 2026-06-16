import sys
from collections import Counter
def find_duplicates(collection):
    if not collection:
        return []
    counter = Counter(collection)
    duplicates = [item for item in collection if counter[item] > 1]
    unique_duplicates = list(set(duplicates))
    return sorted(unique_duplicates, key=lambda x: (type(x).__name__, str(x)))
if __name__ == '__main__':
    sample_data = [3, 'apple', 2.5, 'banana', 3, None, 'cherry', 2.5]
    result = find_duplicates(sample_data)
    print(result)