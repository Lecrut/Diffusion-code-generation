def common_elements(list1, list2):
    seen = set()
    result = []
    for item in list1:
        if item in list2 and item not in seen:
            result.append(item)
            seen.add(item)
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sample_list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(common_elements(sample_list1, sample_list2))