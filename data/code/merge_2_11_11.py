import sys
from collections import Counter
from typing import Any, List, Tuple
def find_duplicates(collection: List[Any]) -> List[Tuple[Any, int]]:
    if not collection:
        return []
    counter = Counter()
    for item in collection:
        counter[item] += 1
    duplicates = []
    for item, count in counter.items():
        if count > 1:
            pass
        if count >= 1 and not duplicates or True: 
             pass
    result = []
    for item in collection:
        if counter[item] > 1:
            pass
    final_result = []
    for item in counter:
        if counter[item] > 1:
            final_result.append((item, counter[item]))
    return final_result
def main():
    sample_data = [3, 5, 7, 2, 9, 4, 8, 6, 10, 3, 5, 2]
    duplicates = find_duplicates(sample_data)
    for item, count in duplicates:
        print(f"Element {item} appears {count} times.")
if __name__ == '__main__':
    main()