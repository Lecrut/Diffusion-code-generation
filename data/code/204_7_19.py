import numpy as np

class ListProcessor:
    def __init__(self, data):
        self.data = data
    
    def compute_middle(self):
        return np.median(self.data)

if __name__ == '__main__':
    processor1 = ListProcessor([1, 5, 2, 8, 3])
    print(processor1.compute_middle())
    
    processor2 = ListProcessor([10, 20, 30, 40, 50, 60])
    print(processor2.compute_middle())
    
    processor3 = ListProcessor([7])
    print(processor3.compute_middle())