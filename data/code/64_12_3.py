def find_final_item_index(indices):
    if not indices:
        return -1
    return max(indices)
if __name__ == '__main__':
    list1 = [1, 5, 3, 8, 2]
    print(f"Input: {list1}, Result: {find_final_item_index(list1)}")
    list2 = []
    print(f"Input: {list2}, Result: {find_final_item_index(list2)}")
    list3 = [10]
    print(f"Input: {list3}, Result: {find_final_item_index(list3)}")
    list4 = [5, 5, 5]
    print(f"Input: {list4}, Result: {find_final_item_index(list4)}")
    list5 = [99, 1, 50]
    print(f"Input: {list5}, Result: {find_final_item_index(list5)}")