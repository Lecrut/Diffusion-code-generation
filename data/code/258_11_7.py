def compute_pair_averages(list1, list2):
    averages = []
    for num1, num2 in zip(list1, list2):
        average = (num1 + num2) / 2
        averages.append(average)
    return averages

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [40, 50, 60]
    result = compute_pair_averages(sample_list1, sample_list2)
    print(result)