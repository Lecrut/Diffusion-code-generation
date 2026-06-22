class SumComparator:
    @staticmethod
    def calculate_sum(numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    @classmethod
    def are_sums_different(cls, list1, list2):
        sum1 = cls.calculate_sum(list1)
        sum2 = cls.calculate_sum(list2)
        return sum1 != sum2

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [5, 15, 25, 35, 45]
    result = SumComparator.are_sums_different(sample_list1, sample_list2)
    print(result)