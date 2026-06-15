def average_of_sets(list_of_sets):
    if not list_of_sets:
        return 0
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        for num in s:
            total_sum += num
            total_count += 1
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    data1 = [ {1, 2}, {3, 4} ]
    data2 = [ {5}, {6, 7, 8} ]
    data3 = []
    data4 = [ set(), {10} ]
    print(f"Average of data1: {average_of_sets(data1)}")
    print(f"Average of data2: {average_of_sets(data2)}")
    print(f"Average of data3: {average_of_sets(data3)}")
    print(f"Average of data4: {average_of_sets(data4)}")