def find_common_elements(list1, list2):
    common = []
    seen = set()
    for item in list1:
        if item in list2 and item not in seen:
            common.append(item)
            seen.add(item)
    return common

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [40, 50, 60, 70, 80]
    result1 = find_common_elements(sample_list1, sample_list2)
    print(f"Common elements of {sample_list1} and {sample_list2}: {result1}")

    sample_list3 = ['apple', 'banana', 'cherry']
    sample_list4 = ['banana', 'date', 'fig']
    result2 = find_common_elements(sample_list3, sample_list4)
    print(f"Common elements of {sample_list3} and {sample_list4}: {result2}")