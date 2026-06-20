class NumberDifference:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compute_difference(self):
        return abs(self.x - self.y)

if __name__ == '__main__':
    diff_instance1 = NumberDifference(10, 5)
    print(diff_instance1.compute_difference())
    
    diff_instance2 = NumberDifference(3.5, 2.5)
    print(diff_instance2.compute_difference())