class StatisticsCalculator:
    def calculate_mean(self, data):
        if not data:
            return None
        total_sum = sum(data)
        count = len(data)
        mean_value = total_sum / count
        return mean_value

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data1 = [10, 20, 30, 40, 50]
    print(calculator.calculate_mean(sample_data1))
    
    sample_data2 = []
    print(calculator.calculate_mean(sample_data2))