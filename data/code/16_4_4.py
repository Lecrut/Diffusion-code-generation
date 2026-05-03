def check_all_positive(numbers):
    return all(n > 0 for n in numbers)
if __name__ == '__main__':
    list1 = [1, 5, 10, 2]
    list2 = [1, -5, 10, 2]
    list3 = [0, 5, 10, 2]
    list4 = []
    list5 = [100]
    print(f"List 1: {list1}, Result: {check_all_positive(list1)}")
    print(f"List 2: {list2}, Result: {check_all_positive(list2)}")
    print(f"List 3: {list3}, Result: {check_all_positive(list3)}")
    print(f"List 4: {list4}, Result: {check_all_positive(list4)}")
    print(f"List 5: {list5}, Result: {check_all_positive(list5)}")