class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    empty_list = []
    print(f"Average of {list1}: {calculator.calculate_average(list1)}")
    print(f"Average of {list2}: {calculator.calculate_average(list2)}")
    print(f"Average of {empty_list}: {calculator.calculate_average(empty_list)}")