import sys
def find_differences(list1, list2):
    try:
        set1 = set(map(str, list1))
        set2 = set(map(str, list2))
        only_in_first = sorted(set1 - set2)
        only_in_second = sorted(set2 - set1)
        return {
            'only_in_list_1': only_in_first,
            'only_in_list_2': only_in_second,
            'in_both': sorted(list1 & list2),
            'total_unique_items': len(union_of_sets := set1 | set2)
        }
    except Exception:
        return {'error': 'Conversion to string failed'}
if __name__ == '__main__':
    sample_list_1 = [4, 5, 6, 7]
    sample_list_2 = [3, 4, 8, 9]
    result = find_differences(sample_list_1, sample_list_2)
    print("Differences Analysis:")
    if 'error' in result:
        print(f"Error occurred: {result['error']}")
    else:
        print(f"Items only in List 1 (sorted): {result['only_in_list_1']}")
        print(f"Items only in List 2 (sorted): {result['only_in_list_2']}")
        print(f"Common items between lists (sorted): {result['in_both']}")
        print(f"Total unique items across both: {result['total_unique_items']}")