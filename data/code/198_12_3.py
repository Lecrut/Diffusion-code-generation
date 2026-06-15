def find_smallest_across_lists(list_of_lists):
    smallest = float('inf')
    found_any = False
    for sublist in list_of_lists:
        if sublist:
            current_min = min(sublist)
            if current_min < smallest:
                smallest = current_min
            found_any = True
    if not found_any:
        return None
    else:
        return smallest
if __name__ == '__main__':
    sample1 = [[1, 5, 10], [2, 8]]
    sample2 = [[-5, -10], [0, 3, -1]]
    sample3 = [[100], [], [-50, -100]]
    sample4 = [[5], [], []]
    sample5 = []
    print(f"Sample 1: {find_smallest_across_lists(sample1)}")
    print(f"Sample 2: {find_smallest_across_lists(sample2)}")
    print(f"Sample 3: {find_smallest_across_lists(sample3)}")
    print(f"Sample 4: {find_smallest_across_lists(sample4)}")
    print(f"Sample 5: {find_smallest_across_lists(sample5)}")