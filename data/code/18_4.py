def check_max_vs_second_to_last(numbers):
    if len(numbers) < 2:
        return False
    maximum = max(numbers)
    second_to_last = numbers[-2]
    return maximum > second_to_last
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 20, 5, 15]
    list3 = [5, 5, 5, 5]
    list4 = [1, 2, 3]
    list5 = [10, 10]
    list6 = [1, 100, 50]
    print(f"List 1: {list1}, Result: {check_max_vs_second_to_last(list1)}")
    print(f"List 2: {list2}, Result: {check_max_vs_second_to_last(list2)}")
    print(f"List 3: {list3}, Result: {check_max_vs_second_to_last(list3)}")
    print(f"List 4: {list4}, Result: {check_max_vs_second_to_last(list4)}")
    print(f"List 5: {list5}, Result: {check_max_vs_second_to_last(list5)}")
    print(f"List 6: {list6}, Result: {check_max_vs_second_to_last(list6)}")