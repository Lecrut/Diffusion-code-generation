def calculate_averages(list1, list2):
    averages = []
    for a, b in zip(list1, list2):
        pair_average = (a + b) / 2
        averages.append(pair_average)
    return averages

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [14, 16, 18]
    result = calculate_averages(sample_list1, sample_list2)
    print(result)