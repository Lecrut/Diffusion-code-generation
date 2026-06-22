def calculate_averages(list1, list2):
    return [(a + b) / 2 for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [15, 25, 35]
    print(calculate_averages(sample_list1, sample_list2))