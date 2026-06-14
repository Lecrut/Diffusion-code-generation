import itertools
def calculate_average_of_multiple_sets(list_of_lists):
    all_elements = itertools.chain.from_iterable(list_of_lists)
    total_sum = sum(all_elements)
    total_count = sum(len(lst) for lst in list_of_lists)
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [4, 5]
    data3 = [6, 7, 8, 9]
    sets = [data1, data2, data3]
    average = calculate_average_of_multiple_sets(sets)
    print(average)