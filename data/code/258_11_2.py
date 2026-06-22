def calculate_averages(list1, list2):
    averages = [a + b for a, b in zip(list1, list2)]
    return [avg / 2 for avg in averages]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    print(calculate_averages(sample_list1, sample_list2))