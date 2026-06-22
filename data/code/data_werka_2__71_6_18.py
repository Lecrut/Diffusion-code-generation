class MedianCalculator:
    def __init__(self, numbers):
        self.numbers = list(numbers)
    
    def calculate(self):
        if not self.numbers:
            return None
        sorted_nums = sorted(self.numbers)
        count = len(sorted_nums)
        if count % 2 == 1:
            return sorted_nums[count // 2]
        else:
            return sorted_nums[count // 2 - 1]

if __name__ == '__main__':
    calc1 = MedianCalculator([10, 20, 30, 40, 50])
    print(calc1.calculate())
    
    calc2 = MedianCalculator([12, 3, 1, 2, 6, 7])
    print(calc2.calculate())
    
    calc3 = MedianCalculator([99])
    print(calc3.calculate())
    
    calc4 = MedianCalculator([4, 8, 1, 5])
    print(calc4.calculate())