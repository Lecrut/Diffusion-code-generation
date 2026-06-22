class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        return min(self.data)

if __name__ == '__main__':
    finder1 = MinFinder([3, 1, 4, 1, 5, 9, 2])
    print(finder1.find_min())
    
    finder2 = MinFinder([-10, 0, 50, -3])
    print(finder2.find_min())
    
    finder3 = MinFinder([42])
    print(finder3.find_min())