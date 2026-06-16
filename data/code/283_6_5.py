def check_positive(data):
    for x in data:
        if x <= 0:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 5, 10, 2]
    list2 = [1, 5, -3, 2]
    list3 = [10, 20, 30]
    list4 = [-1, 5, 10]
    print(f"List 1 is all positive: {check_positive(list1)}")
    print(f"List 2 is all positive: {check_positive(list2)}")
    print(f"List 3 is all positive: {check_positive(list3)}")
    print(f"List 4 is all positive: {check_positive(list4)}")