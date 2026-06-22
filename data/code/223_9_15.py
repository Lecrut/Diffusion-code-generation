import numpy as np

class MaxFinder:
    def __init__(self, data):
        self.data = data
    
    def find_max(self):
        return np.max(self.data)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    finder = MaxFinder(sample_data)
    print(finder.find_max())