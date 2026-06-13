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
    else:
        return smallest
if __name__ == '__main__':
    data1 = [[-5, 10], [3, -8]]
    data2 = [[1, 2, 3], [-10, 5]]
    data3 = [[100], [], [-50, 200]]
    data4 = [[1, 2], [3, 4]]
    data5 = [[-1, -2], [5, 6]]
    data6 = []
    data7 = [[]]
    print(f"Data 1: {find_absolute_smallest(data1)}")
    print(f"Data 2: {find_absolute_smallest(data2)}")
    print(f"Data 3: {find_absolute_smallest(data3)}")
    print(f"Data 4: {find_absolute_smallest(data4)}")
    print(f"Data 5: {find_absolute_smallest(data5)}")
    print(f"Data 6 (Empty input): {find_absolute_smallest(data6)}")
    print(f"Data 7 (Only empty lists): {find_absolute_smallest(data7)}")