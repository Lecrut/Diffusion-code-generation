def sum_elements(lst):
    return sum(lst)

class Calculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Sum of elements using function:", sum_elements(sample_list))
    
    calc_instance = Calculator()
    print("Sum of elements using class method:", calc_instance.calculate_sum([6, 7, 8, 9, 10]))