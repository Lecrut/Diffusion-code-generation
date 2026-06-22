class StatisticsCalculator:
    def get_average(self, data):
        if not data:
            return 0
        total = sum(data)
        count = len(data)
        return total / count

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10.5, 20.0, 35.5, 40.0, 5.5]
    average = calculator.get_average(sample_data)
    print(f"The average of the sample data is: {average}")