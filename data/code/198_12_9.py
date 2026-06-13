def find_absolute_smallest(list_of_lists):
    smallest = float('inf')
    found_any = False
    for sublist in list_of_lists:
        if sublist:
            current_min = min(abs(x) for x in sublist)
            if current_min < smallest:
                smallest = current_min
            found_any = True
    if not found_any:
        return None
    return smallest
if __name__ == '__main__':
    sample1 = [[-5, 2], [8, -10], [3]]
    sample2 = [[100], [-50, 200], [], [99]]
    sample3 = [[1, 2, 3], [-10, -5], []]
    sample4 = [[10], [20], [30]]
    sample5 = [[-1], [5], [-100]]
    sample6 = []
    print(f"Sample 1: {find_absolute_smallest(sample1)}")
    print(f"Sample 2: {find_absolute_smallest(sample2)}")
    print(f"Sample 3: {find_absolute_smallest(sample3)}")
    print(f"Sample 4: {find_absolute_smallest(sample4)}")
    print(f"Sample 5: {find_absolute_smallest(sample5)}")
    print(f"Sample 6: {find_absolute_smallest(sample6)}")