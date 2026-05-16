def contains_zero(numbers):
    for number in numbers:
        if number == 0:
            return True
    return False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 0, 20, 30]
    list3 = [7, 8, 9, 0, 1]
    list4 = [5, 5, 5, 5]
    list5 = []
    print(f"List {list1}: {contains_zero(list1)}")
    print(f"List {list2}: {contains_zero(list2)}")
    print(f"List {list3}: {contains_zero(list3)}")
    print(f"List {list4}: {contains_zero(list4)}")
    print(f"List {list5}: {contains_zero(list5)}")