def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_list1 = [34, 7, 23, 32, 5, 62]
    sample_list2 = [-5, -10, -3, -1, -45]
    sample_list3 = []
    sample_list4 = [100]

    print(f"Smallest in {sample_list1}: {find_smallest(sample_list1)}")
    print(f"Smallest in {sample_list2}: {find_smallest(sample_list2)}")
    print(f"Smallest in {sample_list3}: {find_smallest(sample_list3)}")
    print(f"Smallest in {sample_list4}: {find_smallest(sample_list4)}")