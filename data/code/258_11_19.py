def compute_pair_averages(list1, list2):
    averages = []
    for val1, val2 in zip(list1, list2):
        avg = (val1 + val2) / 2
        averages.append(avg)
    return averages

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [3, 4, 5]
    result = compute_pair_averages(sample_list1, sample_list2)
    print(result)