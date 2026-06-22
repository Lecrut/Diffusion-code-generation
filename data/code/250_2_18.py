class AverageCalculator:
    def calculate(self, data_tuple):
        if not data_tuple:
            return 0
        return sum(data_tuple) / len(data_tuple)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data1 = (10, 20, 30, 40, 50)
    average1 = calculator.calculate(sample_data1)
    print(f"The average of {sample_data1} is: {average1}")
    
    sample_data2 = (5, 15, 25, 35)
    average2 = calculator.calculate(sample_data2)
    print(f"The average of {sample_data2} is: {average2}")
    
    sample_data3 = ()
    average3 = calculator.calculate(sample_data3)
    print(f"The average of {sample_data3} is: {average3}")