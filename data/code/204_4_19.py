import bisect

class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def get_middle(self):
        n = len(self.data)
        if n == 0:
            raise ValueError("Cannot find the middle of an empty list")
        return self.data[n // 2]

if __name__ == '__main__':
    analyzer1 = ListAnalyzer([1, 2, 3, 4, 5])
    print(f"Middle of [1, 2, 3, 4, 5]: {analyzer1.get_middle()}")
    
    analyzer2 = ListAnalyzer([10, 20, 30, 40, 50, 60])
    print(f"Middle of [10, 20, 30, 40, 50, 60]: {analyzer2.get_middle()}")
    
    analyzer3 = ListAnalyzer([1, 2, 3, 4])
    try:
        print(f"Middle of [1, 2, 3, 4]: {analyzer3.get_middle()}")
    except ValueError as e:
        print(e)