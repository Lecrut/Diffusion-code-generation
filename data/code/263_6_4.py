def check_order(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 2, 2, 3, 5]
    list2 = [1, 3, 2, 5]
    list3 = [10, 5, 2]
    list4 = [4, 4, 4]
    list5 = []
    list6 = [5]
    print(f"List {list1} is sorted: {check_order(list1)}")
    print(f"List {list2} is sorted: {check_order(list2)}")
    print(f"List {list3} is sorted: {check_order(list3)}")
    print(f"List {list4} is sorted: {check_order(list4)}")
    print(f"List {list5} is sorted: {check_order(list5)}")
    print(f"List {list6} is sorted: {check_order(list6)}")