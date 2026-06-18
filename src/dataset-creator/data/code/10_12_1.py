class SumCalculator:
    def calculate_sum(self, iterable):
        total = 0
        for item in iterable:
            total += item
        return total
if __name__ == '__main__':
    calculator = SumCalculator()
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = (10, 20, 30)
    empty_list = []
    print(f"Sum of {numbers1}: {calculator.calculate_sum(numbers1)}")
    print(f"Sum of {numbers2}: {calculator.calculate_sum(numbers2)}")
    print(f"Sum of {empty_list}: {calculator.calculate_sum(empty_list)}")