class DataCalculator:
    def __init__(self, data):
        self.data = data
    
    def calculate_mean(self):
        if not self.data:
            return None
        
        total = sum(self.data)
        count = len(self.data)
        
        return total / count

if __name__ == '__main__':
    calculator = DataCalculator([10, 20, 30, 40])
    print(calculator.calculate_mean())