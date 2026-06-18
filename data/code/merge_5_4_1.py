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
    sample_list1 = [1, 5, 2, 8, 3]
    result1 = difference_largest_smallest(sample_list1)
    print(result1)
    sample_list2 = [10, -5, 20, 0, 15]
    result2 = difference_largest_smallest(sample_list2)
    print(result2)
    sample_list3 = [7]
    result3 = difference_largest_smallest(sample_list3)
    print(result3)
    sample_list4 = []
    result4 = difference_largest_smallest(sample_list4)
    print(result4)