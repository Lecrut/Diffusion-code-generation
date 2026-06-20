class NumberGap:
    def __init__(self, num1=20, num2=15):
        self.num1 = num1
        self.num2 = num2
    
    def calculate_gap(self):
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    gap_instance = NumberGap()
    print(gap_instance.calculate_gap())