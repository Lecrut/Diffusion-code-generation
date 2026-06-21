def find_smallest_integer(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_list1 = [34, 23, 56, 78, -1, 90]
    sample_list2 = [-2, -5, -3, -7, -4]
    sample_list3 = [10]
    sample_list4 = []

    print(f"Smallest in {sample_list1}: {find_smallest_integer(sample_list1)}")
    print(f"Smallest in {sample_list2}: {find_smallest_integer(sample_list2)}")
    print(f"Smallest in {sample_list3}: {find_smallest_integer(sample_list3)}")
    print(f"Smallest in {sample_list4}: {find_smallest_integer(sample_list4)}")