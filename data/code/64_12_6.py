def find_final_item_index(indices):
    if not indices:
        return -1
    return max(indices)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(f"Input: {list1}, Result: {find_final_item_index(list1)}")
    list2 = []
    print(f"Input: {list2}, Result: {find_final_item_index(list2)}")
    list3 = [10]
    print(f"Input: {list3}, Result: {find_final_item_index(list3)}")
    list4 = [5, 5, 5]
    print(f"Input: {list4}, Result: {find_final_item_index(list4)}")
    list5 = [-1, 0, -5]
    print(f"Input: {list5}, Result: {find_final_item_index(list5)}")