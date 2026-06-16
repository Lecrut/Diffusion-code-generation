import sys
from collections import Counter
def find_duplicates(collection):
    if not collection:
        return []
    counter = Counter(collection)
    duplicates = [item for item in collection if counter[item] > 1]
    unique_items_with_counts = [(item, count) for item, count in counter.items() if count > 1]
    return {
        'duplicates': list(set(duplicates)),
        'counts': dict(unique_items_with_counts),
        'total_duplicates_count': sum(count - 1 for _, count in unique_items_with_counts)
    }
if __name__ == '__main__':
    sample_data = [3, 5, 7, 2, 9, 4, 8, 6, 10] + list(range(1, 11)) * 2
    result = find_duplicates(sample_data)
    print("Duplicate items found:")
    for item in sorted(result['duplicates']):
        count = result['counts'][item]
        occurrences_in_list = sample_data.count(item) if isinstance(sample_data, list) else sum(1 for x in sample_data if x == item)
        print(f"  {item}: appears {occurrences_in_list} times")