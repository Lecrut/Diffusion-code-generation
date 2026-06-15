import itertools
def calculate_average_of_sets(list_of_lists):
    all_elements = itertools.chain.from_iterable(list_of_lists)
    total_sum = sum(all_elements)
    total_count = sum(len(lst) for lst in list_of_lists)
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    sets = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    average = calculate_average_of_sets(sets)
    print(average)