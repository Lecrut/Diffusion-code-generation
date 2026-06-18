import sys
from collections import Counter
def find_duplicates(collection):
    counter = Counter()
    duplicates_map = {}                                   
    for idx, item in enumerate(collection):
        if item in counter:
            if item not in duplicates_map:
                duplicates_map[item] = []
            duplicates_map[item].append(idx)
        else:
            counter[item] += 1
    return duplicates_map
if __name__ == '__main__':
    sample_data = [3, 5, 7, 2, 9, 4, 8, 6, 10, 3, 5, 7, 2, 9]
    result = find_duplicates(sample_data)
    if not result:
        print("No duplicates found.")
    else:
        for dup_elem in sorted(result.keys()):
            indices = result[dup_elem]
            count = len(indices) - 1
            print(f"Element {dup_elem} appears multiple times at indices: {indices}")