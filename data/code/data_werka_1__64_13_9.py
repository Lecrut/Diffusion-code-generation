def find_final_index(indices):
    if not indices:
        return -1
    index_map = {index: True for index in indices}
    max_index = max(index_map.keys())
    return max_index

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5]
    print(find_final_index(list1))
    list2 = [9, 8, 7, 6, 5]
    print(find_final_index(list2))
    list3 = []
    print(find_final_index(list3))
    list4 = [23, 45, 67, 89]
    print(find_final_index(list4))