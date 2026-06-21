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
    sample_data = [10, 20, 30, 40, 50]
    empty_list = []
    
    print("Mean of sample data:", calculator.calculate_mean(sample_data))
    print("Mean of empty list:", calculator.calculate_mean(empty_list))