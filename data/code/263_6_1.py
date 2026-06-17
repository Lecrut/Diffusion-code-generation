def check_order(data):
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 7, 5, 9]
    list3 = [2, 2, 3, 5]
    list4 = [5, 5, 5]
    list5 = []
    list6 = [10]
    print(f"List {list1} is sorted: {check_order(list1)}")
    print(f"List {list2} is sorted: {check_order(list2)}")
    print(f"List {list3} is sorted: {check_order(list3)}")
    print(f"List {list4} is sorted: {check_order(list4)}")
    print(f"List {list5} is sorted: {check_order(list5)}")
    print(f"List {list6} is sorted: {check_order(list6)}")