def check_max_vs_second_to_last(data):
    if len(data) < 2:
        return False
    maximum = max(data)
    second_to_last = data[-2]
    return maximum > second_to_last
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 2, 5, 1, 9]
    list3 = [5, 5, 5, 5]
    list4 = [1, 2, 3]
    list5 = [100, 10, 50]
    print(f"List 1: {list1}, Result: {check_max_vs_second_to_last(list1)}")
    print(f"List 2: {list2}, Result: {check_max_vs_second_to_last(list2)}")
    print(f"List 3: {list3}, Result: {check_max_vs_second_to_last(list3)}")
    print(f"List 4: {list4}, Result: {check_max_vs_second_to_last(list4)}")
    print(f"List 5: {list5}, Result: {check_max_vs_second_to_last(list5)}")