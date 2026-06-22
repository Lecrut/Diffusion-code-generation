class DifferenceCalculator:
    @staticmethod
    def calculate_difference_sum(list1, list2):
        min_length = min(len(list1), len(list2))
        return sum(list1[i] - list2[i] for i in range(min_length))

if __name__ == '__main__':
    sample_list1 = [2, 4, 6, 8]
    sample_list2 = [1, 3, 5, 7, 9]
    result = DifferenceCalculator.calculate_difference_sum(sample_list1, sample_list2)
    print(result)