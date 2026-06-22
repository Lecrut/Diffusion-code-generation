def are_all_even(numbers):
    return all(num % 2 == 0 for num in numbers)

if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [2, 3, 6, 8]
    print(f"All elements in {list1} are even: {are_all_even(list1)}")
    print(f"All elements in {list2} are even: {are_all_even(list2)}")