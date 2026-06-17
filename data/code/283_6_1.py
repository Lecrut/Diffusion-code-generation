def check_all_positive(data):
    for x in data:
        if x <= 0:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, -2, 3, 4]
    list3 = [1, 5, 0, 8]
    list4 = []
    list5 = [7.5, 100.1, 0.001]
    print(f"List 1: {check_all_positive(list1)}")
    print(f"List 2: {check_all_positive(list2)}")
    print(f"List 3: {check_all_positive(list3)}")
    print(f"List 4: {check_all_positive(list4)}")
    print(f"List 5: {check_all_positive(list5)}")