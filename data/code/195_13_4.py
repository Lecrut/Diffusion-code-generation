def set_difference(list1, list2):
    unique_elements = []
    for item in list1:
        if item not in list2:
            unique_elements.append(item)
    return unique_elements

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(set_difference(sample_list1, sample_list2))