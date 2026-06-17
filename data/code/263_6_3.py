def check_order(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 2, 3, 4, 5]
    list3 = [5, 3, 1]
    list4 = [2, 2, 2, 1]
    list5 = []
    list6 = [10]
    print(f"list1 is sorted: {check_order(list1)}")
    print(f"list2 is sorted: {check_order(list2)}")
    print(f"list3 is sorted: {check_order(list3)}")
    print(f"list4 is sorted: {check_order(list4)}")
    print(f"list5 is sorted: {check_order(list5)}")
    print(f"list6 is sorted: {check_order(list6)}")