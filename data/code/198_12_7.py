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
    sample1 = [[-5, 2], [10, -1]]
    sample2 = [[3, 7], [-10, 0], [5]]
    sample3 = [[100, 200], [], [-50]]
    sample4 = [[1, 2, 3], [4, 5, 6]]
    sample5 = []
    sample6 = [[]]
    sample7 = [[-10], [5], [-20]]
    print(f"Sample 1: {find_absolute_smallest(sample1)}")
    print(f"Sample 2: {find_absolute_smallest(sample2)}")
    print(f"Sample 3: {find_absolute_smallest(sample3)}")
    print(f"Sample 4: {find_absolute_smallest(sample4)}")
    print(f"Sample 5: {find_absolute_smallest(sample5)}")
    print(f"Sample 6: {find_absolute_smallest(sample6)}")
    print(f"Sample 7: {find_absolute_smallest(sample7)}")