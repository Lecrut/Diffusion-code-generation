class SumCalculator:
    def calculate_sum(self, numbers):
        total = 0
        for number in numbers:
            total += number
        return total
if __name__ == '__main__':
    calculator = SumCalculator()
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (10, 20, 30)
    empty_list = []
    single_element = [99]
    sum1 = calculator.calculate_sum(list1)
    sum2 = calculator.calculate_sum(tuple2)
    sum_empty = calculator.calculate_sum(empty_list)
    sum_single = calculator.calculate_sum(single_element)
    print(f"Sum of {list1}: {sum1}")
    print(f"Sum of {tuple2}: {sum2}")
    print(f"Sum of {empty_list}: {sum_empty}")
    print(f"Sum of {single_element}: {sum_single}")