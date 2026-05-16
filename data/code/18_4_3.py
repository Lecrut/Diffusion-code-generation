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
    list5 = [100, 50, 200]
    print(f"List {list1}: {check_max_vs_second_to_last(list1)}")
    print(f"List {list2}: {check_max_vs_second_to_last(list2)}")
    print(f"List {list3}: {check_max_vs_second_to_last(list3)}")
    print(f"List {list4}: {check_max_vs_second_to_last(list4)}")
    print(f"List {list5}: {check_max_vs_second_to_last(list5)}")