def difference_largest_smallest(numbers):
    if not numbers:
        return 0
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    return largest - smallest
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(difference_largest_smallest(list1))
    list2 = [10, 4, 7, 1, 9]
    print(difference_largest_smallest(list2))
    list3 = [5]
    print(difference_largest_smallest(list3))
    list4 = []
    print(difference_largest_smallest(list4))