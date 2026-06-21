class SumCalculator:
    @staticmethod
    def calculate_sum(data):
        return sum(data)

if __name__ == '__main__':
    my_list = [1, 5, 10, 2.5]
    result = SumCalculator.calculate_sum(my_list)
    print(result)