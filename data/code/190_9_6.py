def contains_negative(numbers):
    for number in numbers:
        if number < 0:
            return True
    return False
if __name__ == '__main__':
    list1 = [1, 2, 3, -4, 5]
    list2 = [10, 20, 30]
    list3 = [-1, -5, 100]
    list4 = []
    list5 = [0, 5, -2]
    print(f"List 1 contains negative: {contains_negative(list1)}")
    print(f"List 2 contains negative: {contains_negative(list2)}")
    print(f"List 3 contains negative: {contains_negative(list3)}")
    print(f"List 4 contains negative: {contains_negative(list4)}")
    print(f"List 5 contains negative: {contains_negative(list5)}")