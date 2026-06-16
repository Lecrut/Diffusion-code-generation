import sys
from collections import Counter
def find_duplicates(collection):
    counter = Counter(collection)
    duplicates = [item for item in collection if counter[item] > 1]
    return list(set(duplicates))
if __name__ == '__main__':
    sample_data = [3, 5, 7, 2, 9, 4, 8, 6, 10, 3, 5, 7, 2, 9]
    result = find_duplicates(sample_data)
    print(result)