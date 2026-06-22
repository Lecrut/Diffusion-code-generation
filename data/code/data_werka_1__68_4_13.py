class DifferenceCalculator:
    @staticmethod
    def calculate(list1, list2):
        result = {}
        for i in range(min(len(list1), len(list2))):
            result[i] = list1[i] - list2[i]
        return result

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [2, 5, 10, 15]
    difference_dict = DifferenceCalculator.calculate(sample_list1, sample_list2)
    print(difference_dict)