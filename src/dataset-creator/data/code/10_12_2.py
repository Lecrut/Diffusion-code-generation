class SumCalculator:
    def calculate_sum(self, iterable):
        total = 0
        for item in iterable:
            total += item
        return total
if __name__ == '__main__':
    calculator = SumCalculator()
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (10, 20, 30)
    empty_list = []
    negative_numbers = [-1, 5, -3]
    sum1 = calculator.calculate_sum(list1)
    sum2 = calculator.calculate_sum(tuple2)
    sum_empty = calculator.calculate_sum(empty_list)
    sum_neg = calculator.calculate_sum(negative_numbers)
    print(f"Sum of {list1}: {sum1}")
    print(f"Sum of {tuple2}: {sum2}")
    print(f"Sum of {empty_list}: {sum_empty}")
    print(f"Sum of {negative_numbers}: {sum_neg}")