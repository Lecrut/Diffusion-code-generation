class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return None
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    empty_list = []
    
    avg1 = calculator.calculate_average(list1)
    print(f"The average of {list1} is: {avg1}")
    
    avg2 = calculator.calculate_average(list2)
    print(f"The average of {list2} is: {avg2}")
    
    avg3 = calculator.calculate_average(empty_list)
    print(f"The average of {empty_list} is: {avg3}")