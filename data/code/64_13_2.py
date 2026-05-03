def find_final_index(indices):
    if not indices:
        return -1
    return indices[-1]
if __name__ == '__main__':
    list1 = [1, 5, 3, 8, 2]
    print(find_final_index(list1))
    list2 = [100]
    print(find_final_index(list2))
    list3 = []
    print(find_final_index(list3))
    list4 = [42, 99, 12, 55]
    print(find_final_index(list4))