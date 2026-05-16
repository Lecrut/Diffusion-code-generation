def check_all_positive(numbers):
    return all(n > 0 for n in numbers)
if __name__ == '__main__':
    list1 = [1, 5, 10, 2]
    list2 = [1, -5, 10, 2]
    list3 = [0, 5, 10, 2]
    list4 = []
    list5 = [1, 2, 3]
    print(f"List 1: {check_all_positive(list1)}")
    print(f"List 2: {check_all_positive(list2)}")
    print(f"List 3: {check_all_positive(list3)}")
    print(f"List 4: {check_all_positive(list4)}")
    print(f"List 5: {check_all_positive(list5)}")