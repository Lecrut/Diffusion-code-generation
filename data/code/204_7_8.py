import numpy as np

class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def find_middle(self):
        return np.median(self.data)

if __name__ == '__main__':
    analyzer1 = ListAnalyzer([1, 5, 2, 8, 3])
    print(analyzer1.find_middle())
    
    analyzer2 = ListAnalyzer([10, 20, 30, 40, 50, 60])
    print(analyzer2.find_middle())
    
    analyzer3 = ListAnalyzer([7])
    print(analyzer3.find_middle())
    
    analyzer4 = ListAnalyzer([])
    print(analyzer4.find_middle())