class MeanCalculator:
    def compute_mean(self, data):
        if not data:
            return None
        return sum(data) / len(data)

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_data1 = [10, 20, 30, 40, 50]
    sample_data2 = [10.5, 20.25, 30.75]
    
    mean_value1 = calculator.compute_mean(sample_data1)
    mean_value2 = calculator.compute_mean(sample_data2)
    
    print("Mean of sample data 1:", mean_value1)
    print("Mean of sample data 2:", mean_value2)