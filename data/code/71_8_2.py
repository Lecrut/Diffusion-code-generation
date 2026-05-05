def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (data[middle_left_index] + data[middle_right_index]) / 2
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [5.5, 6.5, 7.5, 8.5]
    list4 = [100]
    list5 = []
    list6 = [1, 2, 3, 4]
    print(f"List: {list1}, Middle: {find_middle(list1)}")
    print(f"List: {list2}, Middle: {find_middle(list2)}")
    print(f"List: {list3}, Middle: {find_middle(list3)}")
    print(f"List: {list4}, Middle: {find_middle(list4)}")
    print(f"List: {list5}, Middle: {find_middle(list5)}")
    print(f"List: {list6}, Middle: {find_middle(list6)}")