def find_absolute_smallest(list_of_lists):
    smallest = None
    for sublist in list_of_lists:
        if sublist:
            current_min = min(abs(x) for x in sublist)
            if smallest is None or current_min < smallest:
                smallest = current_min
    return smallest
if __name__ == '__main__':
    sample1 = [[-5, 2], [8, -10], [3]]
    sample2 = [[100], [-50], []]
    sample3 = [[1, 2, 3], [-10, -20], [4]]
    sample4 = [[5], [], [-1]]
    sample5 = [[10], [20], [30]]
    sample6 = [[]]
    print(f"Sample 1: {find_absolute_smallest(sample1)}")
    print(f"Sample 2: {find_absolute_smallest(sample2)}")
    print(f"Sample 3: {find_absolute_smallest(sample3)}")
    print(f"Sample 4: {find_absolute_smallest(sample4)}")
    print(f"Sample 5: {find_absolute_smallest(sample5)}")
    print(f"Sample 6: {find_absolute_smallest(sample6)}")