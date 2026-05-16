def check_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0 and num % 2 == 0:
            count += 1
    return count >= 3
if __name__ == '__main__':
    list1 = [2, 4, 6, 1, 3, 5]
    list2 = [1, 3, 5, 7, 9]
    list3 = [2, 4, 6, 8, 10]
    list4 = [10, 20, 30]
    print(f"List 1: {check_numbers(list1)}")
    print(f"List 2: {check_numbers(list2)}")
    print(f"List 3: {check_numbers(list3)}")
    print(f"List 4: {check_numbers(list4)}")