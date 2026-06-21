import numpy as np

class ArrayAnalyzer:
    def __init__(self, data):
        self.data = np.array(data)
    
    def calculate_mean(self):
        return np.mean(self.data)

if __name__ == '__main__':
    analyzer1 = ArrayAnalyzer([1, 2, 3, 4, 5])
    analyzer2 = ArrayAnalyzer([10.5, 20.5, 30.5])
    analyzer_empty = ArrayAnalyzer([])
    analyzer3 = ArrayAnalyzer([-1, 5, 10, -2])
    
    print(f"Mean of {analyzer1.data}: {analyzer1.calculate_mean()}")
    print(f"Mean of {analyzer2.data}: {analyzer2.calculate_mean()}")
    print(f"Mean of {analyzer_empty.data}: {analyzer_empty.calculate_mean()}")
    print(f"Mean of {analyzer3.data}: {analyzer3.calculate_mean()}")