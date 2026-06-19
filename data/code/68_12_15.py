def find_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference_set = set1 - set2
    return list(difference_set)

if __name__ == '__main__':
    primary_list = [5, 10, 15, 20, 25]
    secondary_list = [10, 20, 30, 40, 50]
    unique_elements = find_difference(primary_list, secondary_list)
    print(unique_elements)