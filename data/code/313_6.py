def is_all_even(numbers):
    for number in numbers:
        if number % 2 != 0:
            return False
    return True
if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [2, 4, 5, 8]
    list3 = [10, 22, 30]
    list4 = []
    list5 = [1, 3, 5]
    print(f"is_all_even({list1}): {is_all_even(list1)}")
    print(f"is_all_even({list2}): {is_all_even(list2)}")
    print(f"is_all_even({list3}): {is_all_even(list3)}")
    print(f"is_all_even({list4}): {is_all_even(list4)}")
    print(f"is_all_even({list5}): {is_all_even(list5)}")