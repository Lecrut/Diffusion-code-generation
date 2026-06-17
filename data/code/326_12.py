class StatisticsCalculator:
    def get_average(self, data_list):
        if not data_list:
            return 0
        return sum(data_list) / len(data_list)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10, 20, 30, 40, 50]
    average = calculator.get_average(sample_data)
    print(average)