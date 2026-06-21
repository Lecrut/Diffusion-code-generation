import statistics

def compare_data_sets(data_set_1, data_set_2):
    mean_1 = statistics.mean(data_set_1)
    median_1 = statistics.median(data_set_1)
    std_dev_1 = statistics.stdev(data_set_1)

    mean_2 = statistics.mean(data_set_2)
    median_2 = statistics.median(data_set_2)
    std_dev_2 = statistics.stdev(data_set_2)

    print(f"Mean of Data Set 1: {mean_1}")
    print(f"Median of Data Set 1: {median_1}")
    print(f"Standard Deviation of Data Set 1: {std_dev_1}")

    print(f"Mean of Data Set 2: {mean_2}")
    print(f"Median of Data Set 2: {median_2}")
    print(f"Standard Deviation of Data Set 2: {std_dev_2}")

if __name__ == '__main__':
    data_set_1 = [1, 2, 3, 4, 5]
    data_set_2 = [5, 4, 3, 2, 1]

    compare_data_sets(data_set_1, data_set_2)