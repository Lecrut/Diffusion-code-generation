import itertools
def calculate_average_of_sets(sets):
    all_elements = itertools.chain(*sets)
    total_sum = sum(all_elements)
    total_count = sum(len(s) for s in sets)
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    set1 = [1, 2, 3]
    set2 = [4, 5]
    set3 = [6, 7, 8, 9]
    sets_to_average = [set1, set2, set3]
    average = calculate_average_of_sets(sets_to_average)
    print(average)