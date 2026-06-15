def sort_three_numbers(numbers):
    numbers.sort()
if __name__ == '__main__':
    list1 = [5, 2, 8]
    print(f"Original list 1: {list1}")
    sort_three_numbers(list1)
    print(f"Sorted list 1: {list1}\n")
    list2 = [100, 42, 34]
    print(f"Original list 2: {list2}")
    sort_three_numbers(list2)
    print(f"Sorted list 2: {list2}\n")
    list3 = [-5, 0, 10]
    print(f"Original list 3: {list3}")
    sort_three_numbers(list3)
    print(f"Sorted list 3: {list3}\n")