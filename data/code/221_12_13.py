class NumberSorter:
    def __init__(self, a, b, c):
        self.numbers = [a, b, c]
    
    @staticmethod
    def sort_numbers(numbers):
        return sorted(numbers)
    
    def get_sorted_values(self):
        return NumberSorter.sort_numbers(self.numbers)

if __name__ == '__main__':
    sorter = NumberSorter(5, 2, 8)
    sorted_list = sorter.get_sorted_values()
    print(sorted_list)