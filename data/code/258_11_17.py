class AverageCalculator:
    @staticmethod
    def calculate_pair_average(pair):
        return sum(pair) / len(pair)

    @staticmethod
    def calculate_averages(list1, list2):
        return [AverageCalculator.calculate_pair_average((a, b)) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    print(AverageCalculator.calculate_averages(sample_list1, sample_list2))