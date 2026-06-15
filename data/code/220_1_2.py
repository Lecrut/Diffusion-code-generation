import itertools
def calculate_average_of_sets(list_of_sets):
    all_elements = set()
    for s in list_of_sets:
        all_elements.update(s)
    if not all_elements:
        return 0.0
    return sum(all_elements) / len(all_elements)
if __name__ == '__main__':
    sample_data = [
        {1, 2, 3},
        {3, 4, 5},
        {5, 6}
    ]
    result = calculate_average_of_sets(sample_data)
    print(result)