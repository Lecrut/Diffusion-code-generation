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
    sample1 = [[1, 5, -3], [10, -20]]
    sample2 = [[100], [-50, 10], []]
    sample3 = [[]]
    sample4 = [[5], [8], [-100]]
    sample5 = [[]]
    print(f"Sample 1: {find_absolute_smallest(sample1)}")
    print(f"Sample 2: {find_absolute_smallest(sample2)}")
    print(f"Sample 3: {find_absolute_smallest(sample3)}")
    print(f"Sample 4: {find_absolute_smallest(sample4)}")
    print(f"Sample 5: {find_absolute_smallest(sample5)}")