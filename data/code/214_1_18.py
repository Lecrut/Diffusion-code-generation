def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 50, -3]
    list3 = []
    list4 = [42]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    print(f"Minimum of {list4}: {find_minimum(list4)}")