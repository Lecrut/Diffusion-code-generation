class NumberSorter:
    def __init__(self, num1, num2, num3):
        self.numbers = [num1, num2, num3]

    def sort_numbers(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    sorter = NumberSorter(5, 1, 8)
    sorted_nums = sorter.sort_numbers()
    print(f"{sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}")