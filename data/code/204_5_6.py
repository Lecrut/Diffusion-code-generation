class MiddleValueFinder:
    def __init__(self, data):
        self.data = sorted(data)

    def get_middle_value(self):
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2

if __name__ == '__main__':
    finder1 = MiddleValueFinder([1, 2, 3, 4, 5])
    print(finder1.get_middle_value())
    
    finder2 = MiddleValueFinder([10, 20, 30, 40])
    print(finder2.get_middle_value())
    
    finder3 = MiddleValueFinder([100])
    print(finder3.get_middle_value())