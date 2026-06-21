import numpy as np

class ArrayAnalyzer:
    def __init__(self, data):
        self.data = np.array(data)
    
    def calculate_average(self):
        return np.mean(self.data)

if __name__ == '__main__':
    analyzer = ArrayAnalyzer([1.0, 2.0, 3.0, 4.0, 5.0])
    average_result = analyzer.calculate_average()
    print(average_result)