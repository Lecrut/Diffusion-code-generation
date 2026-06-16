def check_all_positive(data):
    for x in data:
        if x <= 0:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 5, 10, 3]
    list2 = [2, -1, 4, 6]
    list3 = [100, 50, 0, 20]
    list4 = [7, 8, 9]
    print(f"List 1: {check_all_positive(list1)}")
    print(f"List 2: {check_all_positive(list2)}")
    print(f"List 3: {check_all_positive(list3)}")
    print(f"List 4: {check_all_positive(list4)}")