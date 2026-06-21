import statistics

class DataComparator:
    @staticmethod
    def calculate_statistics(data):
        return {
            'mean': statistics.mean(data),
            'median': statistics.median(data),
            'std_dev': statistics.stdev(data)
        }

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [3, 4, 5, 6, 7]

    comparator = DataComparator()
    result_set_1 = comparator.calculate_statistics(sample_data_set_1)
    result_set_2 = comparator.calculate_statistics(sample_data_set_2)

    print(f"Sample Data Set 1: {sample_data_set_1}")
    print(f"Sample Data Set 2: {sample_data_set_2}")
    print("Statistics for Sample Data Set 1:")
    print(result_set_1)
    print("Statistics for Sample Data Set 2:")
    print(result_set_2)