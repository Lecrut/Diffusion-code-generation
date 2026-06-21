class AverageCalculator:
    def calculate_average(self, data):
        if not data:
            raise ValueError("Input list is empty")
        
        total = sum(item for item in data)
        count = len(data)
        return total / count

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data1 = [10, 20, 30, 40, 50]
    print(f"Average of {sample_data1}: {calculator.calculate_average(sample_data1)}")
    
    sample_data2 = [5.5, 10, 15.5, 20]
    print(f"Average of {sample_data2}: {calculator.calculate_average(sample_data2)}")