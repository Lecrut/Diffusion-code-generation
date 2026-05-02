def find_final_index(indices):
    if not indices:
        return -1
    return max(indices)
if __name__ == '__main__':
    list1 = [1, 5, 3, 8, 2]
    print(f"Input: {list1}, Result: {find_final_index(list1)}")
    list2 = [100, 50, 200, 150]
    print(f"Input: {list2}, Result: {find_final_index(list2)}")
    list3 = []
    print(f"Input: {list3}, Result: {find_final_index(list3)}")
    list4 = [42]
    print(f"Input: {list4}, Result: {find_final_index(list4)}")
    list5 = [-5, -1, -10]
    print(f"Input: {list5}, Result: {find_final_index(list5)}")