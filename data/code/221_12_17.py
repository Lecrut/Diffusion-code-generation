class NumberSorter:
    def __init__(self, a, b, c):
        self.numbers = [a, b, c]
    
    @staticmethod
    def sort_numbers(numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sorter = NumberSorter(5, 2, 8)
    sorted_list = NumberSorter.sort_numbers(sorter.numbers)
    print(sorted_list)