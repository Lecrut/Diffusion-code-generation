class SumCalculator:
    @staticmethod
    def sum_list(input_list):
        return sum(input_list)

if __name__ == '__main__':
    my_list = [1, 5, 10.5, 2]
    result = SumCalculator.sum_list(my_list)
    print(result)