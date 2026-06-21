def calculate_list_sum(numbers):
    return sum(numbers)

class Calculator:
    def __init__(self):
        self.calculations = []

    def add_calculation(self, numbers, result):
        self.calculations.append((numbers, result))

    def print_calculations(self):
        for inputs, output in self.calculations:
            print(f'Input: {inputs}, Output: {output}')

if __name__ == '__main__':
    calc = Calculator()
    
    list1 = [1, 2, 3, 4, 5]
    result1 = calculate_list_sum(list1)
    calc.add_calculation(list1, result1)
    
    list2 = [10.5, 20.5, 30.0]
    result2 = calculate_list_sum(list2)
    calc.add_calculation(list2, result2)
    
    list3 = [-1, 5, -3, 10]
    result3 = calculate_list_sum(list3)
    calc.add_calculation(list3, result3)
    
    calc.print_calculations()