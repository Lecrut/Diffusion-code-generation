def compute_average(data):
    if not data:
        return 0
    total_sum = sum(data)
    count = len(data)
    if count == 0:
        return 0
    return total_sum / count

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def calculate_average(self):
        return compute_average(self.data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    analyzer = DataAnalyzer(sample_data)
    average = analyzer.calculate_average()
    print(average)