class StatisticsCalculator:
    def get_mean(self, data):
        if not data:
            return None
        total_sum = sum(data)
        count = len(data)
        mean_value = total_sum / count
        return mean_value

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10, 20, 30, 40, 50]
    print("Mean of sample data:", calculator.get_mean(sample_data))
    
    empty_list = []
    print("Mean of empty list:", calculator.get_mean(empty_list))