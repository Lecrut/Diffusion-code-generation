class StatisticsCalculator:
    DEFAULT_AVERAGE = 0

    @staticmethod
    def calculate_average(data_tuple):
        if not data_tuple:
            return StatisticsCalculator.DEFAULT_AVERAGE
        return sum(data_tuple) / len(data_tuple)

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data1 = (10, 20, 30, 40, 50)
    average1 = calculator.calculate_average(sample_data1)
    print(f"The average of {sample_data1} is: {average1}")
    sample_data2 = (5, 15, 25)
    average2 = calculator.calculate_average(sample_data2)
    print(f"The average of {sample_data2} is: {average2}")
    sample_data3 = ()
    average3 = calculator.calculate_average(sample_data3)
    print(f"The average of {sample_data3} is: {average3}")