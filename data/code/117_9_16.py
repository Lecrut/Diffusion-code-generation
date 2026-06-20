class NumberDifference:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def compute_difference(self):
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    diff_instance = NumberDifference(10, 5)
    print(diff_instance.compute_difference())