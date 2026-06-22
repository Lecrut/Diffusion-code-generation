class DifferenceCalculator:
    @staticmethod
    def calculate_difference_sum(list1, list2):
        min_length = min(len(list1), len(list2))
        difference_sum = 0
        for i in range(min_length):
            difference_sum += list1[i] - list2[i]
        return difference_sum

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5]
    sample_list_b = [10, 20, 30, 40]
    result = DifferenceCalculator.calculate_difference_sum(sample_list_a, sample_list_b)
    print(result)