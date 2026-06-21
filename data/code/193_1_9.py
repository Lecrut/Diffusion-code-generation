class ListSumCalculator:
    def calculate_sum(self, iterable):
        total = 0
        for number in iterable:
            total += number
        return total

if __name__ == '__main__':
    calculator = ListSumCalculator()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    list3 = [-1, 5, -10, 2]
    empty_list = []
    print(f"Sum of {list1}: {calculator.calculate_sum(list1)}")
    print(f"Sum of {list2}: {calculator.calculate_sum(list2)}")
    print(f"Sum of {list3}: {calculator.calculate_sum(list3)}")
    print(f"Sum of {empty_list}: {calculator.calculate_sum(empty_list)}")