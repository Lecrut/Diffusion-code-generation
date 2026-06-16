class StatisticsCalculator:
    def get_average(self, data_list):
        if not data_list:
            return 0
        return sum(data_list) / len(data_list)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data1 = [10, 20, 30, 40, 50]
    result1 = calculator.get_average(sample_data1)
    print(f"The average of {sample_data1} is: {result1}")
    sample_data2 = [5, 15, 25]
    result2 = calculator.get_average(sample_data2)
    print(f"The average of {sample_data2} is: {result2}")
    sample_data3 = []
    result3 = calculator.get_average(sample_data3)
    print(f"The average of {sample_data3} is: {result3}")