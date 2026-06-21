class SumCalculator:
    @staticmethod
    def calculate_sum(lst):
        return sum(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(SumCalculator.calculate_sum(sample_list))