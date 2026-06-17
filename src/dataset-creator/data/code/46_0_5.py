import time
def find_differences(list1, list2):
    set1 = set(map(str, list1))
    set2 = set(map(str, list2))
    only_in_list1 = sorted(set1 - set2)
    only_in_list2 = sorted(set2 - set1)
    return {
        'only_in_first': only_in_list1,
        'only_in_second': only_in_list2,
        'common_elements': sorted(list(set1 & set2))
    }
if __name__ == '__main__':
    sample_data_1 = [300.75, 400.80, 600.90]
    sample_data_2 = [300.75, 500.90, 600.90]
    start_time = time.time()
    result = find_differences(sample_data_1, sample_data_2)
    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.4f} seconds")
    if 'only_in_first' in result:
        for item in result['only_in_first']:
            print(item)
    if 'only_in_second' in result:
        for item in result['only_in_second']:
            print(f"{item}")