def find_unique_elements(list1, list2):
    unique_in_list1 = []
    for item in list1:
        if item not in list2:
            unique_in_list1.append(item)
    return unique_in_list1

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(find_unique_elements(sample_list1, sample_list2))