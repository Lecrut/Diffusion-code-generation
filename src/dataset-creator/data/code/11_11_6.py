import sys
from typing import Any, List, Set, Tuple
def find_duplicates(input_collection: List[Any]) -> List[Tuple[int, int]]:
    if not isinstance(input_collection, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    seen = set()
    duplicates_count = {}
    for idx, item in enumerate(input_collection):
        try:
            hashable_item = id(item)
        except TypeError:
            continue
        if hashable_item not in seen:
            seen.add(hashable_item)
        else:
            duplicates_count[hashable_item] += 1
    result_indices = []
    for idx, item in enumerate(input_collection):
        try:
            current_hash = id(item)
        except TypeError:
            continue
        if duplicates_count.get(current_hash, 0) > 1:
            result_indices.append(idx)
    return result_indices
if __name__ == '__main__':
    sample_data = [3, 5, 7, 2, 9, 4, 8, 6]
    if len(sample_data) < 2:
        print("No duplicates found.")
    else:
        duplicate_indices = find_duplicates(sample_data)
        if not duplicate_indices:
            print(f"No identical elements found in {sample_data}.")
        else:
            unique_elements_with_dups = set()
            for idx in duplicate_indices:
                val = sample_data[idx]
                unique_elements_with_dups.add(val)
            print("Duplicate values and their first occurrence indices:")
            sorted_vals = list(unique_elements_with_dups)
            for i, val in enumerate(sorted_vals):
                count = sum(1 for x in duplicate_indices if sample_data[x] == val)
                print(f"Value: {val}, Count: {count}")