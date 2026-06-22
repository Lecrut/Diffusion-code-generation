import numpy as np

class DataAnalyzer:
    def __init__(self):
        self.values = []
    
    def add_values(self, new_values):
        self.values.extend(new_values)
    
    def compute_average(self):
        if not self.values:
            return 0.0
        return np.mean(self.values)

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    analyzer.add_values([100, 200, 300])
    print(analyzer.compute_average())