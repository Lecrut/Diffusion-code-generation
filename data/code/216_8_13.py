class MedianCalculator:
    def __init__(self, data):
        self.data = sorted(data)
    
    def calculate_middle(self):
        n = len(self.data)
        if n == 0:
            raise ValueError("List is empty")
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    calc = MedianCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    print(calc.calculate_middle())