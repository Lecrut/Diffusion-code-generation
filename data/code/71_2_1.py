def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    else:
        middle_index = n // 2
        if n % 2 == 1:
            return data[middle_index]
        else:
            middle1 = data[middle_index - 1]
            middle2 = data[middle_index]
            return (middle1 + middle2) / 2
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 20, 30, 40]
    list3 = [7]
    list4 = []
    list5 = [1, 2, 3, 4, 5, 6]
    print(f"List: {list1}, Middle Value: {find_middle_value(list1)}")
    print(f"List: {list2}, Middle Value: {find_middle_value(list2)}")
    print(f"List: {list3}, Middle Value: {find_middle_value(list3)}")
    print(f"List: {list4}, Middle Value: {find_middle_value(list4)}")
    print(f"List: {list5}, Middle Value: {find_middle_value(list5)}")