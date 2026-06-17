def check_order(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 2, 2, 3, 5]
    list2 = [1, 3, 2, 5]
    list3 = [5, 4, 3, 2, 1]
    list4 = [10]
    list5 = []
    list6 = [7, 7, 7]
    print(f"List {list1}: {check_order(list1)}")
    print(f"List {list2}: {check_order(list2)}")
    print(f"List {list3}: {check_order(list3)}")
    print(f"List {list4}: {check_order(list4)}")
    print(f"List {list5}: {check_order(list5)}")
    print(f"List {list6}: {check_order(list6)}")