def check_max_vs_second_to_last(numbers):
    if len(numbers) < 2:
        return False
    maximum = max(numbers)
    second_to_last = numbers[-2]
    return maximum > second_to_last
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 20, 5, 15]
    list3 = [7, 7, 7, 7]
    list4 = [1, 2]
    list5 = [100, 50, 100]
    print(f"List 1: {list1}, Result: {check_max_vs_second_to_last(list1)}")
    print(f"List 2: {list2}, Result: {check_max_vs_second_to_last(list2)}")
    print(f"List 3: {list3}, Result: {check_max_vs_second_to_last(list3)}")
    print(f"List 4: {list4}, Result: {check_max_vs_second_to_last(list4)}")
    print(f"List 5: {list5}, Result: {check_max_vs_second_to_last(list5)}")