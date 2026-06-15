import itertools
def calculate_average_of_multiple_sets(sets):
    all_elements = itertools.chain.from_iterable(s for s in sets)
    total_sum = sum(all_elements)
    total_count = sum(len(s) for s in sets)
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [4, 5]
    data3 = [6, 7, 8, 9]
    sets_to_average = [data1, data2, data3]
    average = calculate_average_of_multiple_sets(sets_to_average)
    print(average)