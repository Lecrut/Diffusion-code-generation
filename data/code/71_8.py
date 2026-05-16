def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_index_1 = n // 2 - 1
        middle_index_2 = n // 2
        return (data[middle_index_1], data[middle_index_2])
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [50]
    list4 = []
    list5 = [1, 2, 3, 4]
    list6 = [100, 200]
    print(f"List: {list1}, Middle: {find_middle(list1)}")
    print(f"List: {list2}, Middle: {find_middle(list2)}")
    print(f"List: {list3}, Middle: {find_middle(list3)}")
    print(f"List: {list4}, Middle: {find_middle(list4)}")
    print(f"List: {list5}, Middle: {find_middle(list5)}")
    print(f"List: {list6}, Middle: {find_middle(list6)}")