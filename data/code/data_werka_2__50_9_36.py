import numpy as np

class RegionAnalyzer:
    def __init__(self, region1, region2):
        self.region1 = np.array(region1)
        self.region2 = np.array(region2)
        if self.region1.shape != self.region2.shape:
            raise ValueError('Both regions must have the same shape.')

    def area_difference(self):
        xor_result = np.bitwise_xor(self.region1, self.region2)
        return np.sum(xor_result)

if __name__ == '__main__':
    region1 = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    region2 = [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
    
    analyzer = RegionAnalyzer(region1, region2)
    difference = analyzer.area_difference()
    
    print(f"Area Difference: {difference}")