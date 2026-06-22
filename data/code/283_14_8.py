def are_all_even(numbers):
    return all(num % 2 == 0 for num in numbers)

if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [1, 2, 3, 4]
    list3 = [10, 22, 34, 47]
    print(f"All numbers in list1 are even: {are_all_even(list1)}")
    print(f"All numbers in list2 are even: {are_all_even(list2)}")
    print(f"All numbers in list3 are even: {are_all_even(list3)}")