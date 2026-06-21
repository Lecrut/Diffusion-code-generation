class SumComparer:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_sum(self, lst):
        return sum(lst)

    def are_sums_different(self):
        sum1 = self.calculate_sum(self.list1)
        sum2 = self.calculate_sum(self.list2)
        return sum1 != sum2

if __name__ == '__main__':
    sample_list1 = [100, 200, 300]
    sample_list2 = [300, 200, 100]
    comparer = SumComparer(sample_list1, sample_list2)
    result = comparer.are_sums_different()
    print(result)

    another_sample_list1 = [1, 2, 3]
    another_sample_list2 = [4, 5, 6]
    another_comparer = SumComparer(another_sample_list1, another_sample_list2)
    another_result = another_comparer.are_sums_different()
    print(another_result)