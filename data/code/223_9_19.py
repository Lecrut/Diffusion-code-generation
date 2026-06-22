import numpy as np

class MaxFinder:
    def __init__(self, data):
        self.data = np.array(data)

    def find_max(self):
        return np.max(self.data)

if __name__ == '__main__':
    finder = MaxFinder([10, 5, 20, 8, 15])
    print(finder.find_max())