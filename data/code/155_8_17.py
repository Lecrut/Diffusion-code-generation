class SumCalculator:
    def __init__(self):
        self.total_sum = 0

    def add_to_total(self, number):
        self.total_sum += abs(number)

    def get_total_sum(self):
        return self.total_sum

if __name__ == '__main__':
    calculator = SumCalculator()
    
    sample_list1 = [1, -2, 3, -4, 5]
    for num in sample_list1:
        calculator.add_to_total(num)
    
    print(f"Result for {sample_list1}: {calculator.get_total_sum()}")
    
    calculator = SumCalculator()
    sample_list2 = [-10, 0, 5, -2.5]
    for num in sample_list2:
        calculator.add_to_total(num)
    
    print(f"Result for {sample_list2}: {calculator.get_total_sum()}")