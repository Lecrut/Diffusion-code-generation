def calculate_average_of_pairs(list1, list2):
    return [(a + b) / 2 for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    print(calculate_average_of_pairs(sample_list1, sample_list2))