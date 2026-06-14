def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    else:
        middle_index = n // 2
        if n % 2 == 1:
            return data[middle_index]
        else:
            return data[middle_index - 1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [5.5, 6.6, 7.7]
    list4 = [99]
    list5 = []
    list6 = [1, 2, 3, 4]
    list7 = [100, 200]
    print(f"List: {list1}, Middle Value: {find_middle(list1)}")
    print(f"List: {list2}, Middle Value: {find_middle(list2)}")
    print(f"List: {list3}, Middle Value: {find_middle(list3)}")
    print(f"List: {list4}, Middle Value: {find_middle(list4)}")
    print(f"List: {list5}, Middle Value: {find_middle(list5)}")
    print(f"List: {list6}, Middle Value: {find_middle(list6)}")
    print(f"List: {list7}, Middle Value: {find_middle(list7)}")