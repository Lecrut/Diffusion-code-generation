class StatisticsCalculator:
    def get_mean(self, data):
        if not data:
            return None
        return sum(data) / len(data)

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data1 = [10, 20, 30, 40, 50]
    mean_value1 = calculator.get_mean(sample_data1)
    print(mean_value1)
    
    sample_data2 = []
    mean_value2 = calculator.get_mean(sample_data2)
    print(mean_value2)