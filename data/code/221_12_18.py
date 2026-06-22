class NumberSorter:
    def __init__(self, a, b, c):
        self.values = {1: a, 2: b, 3: c}
    
    def sort_numbers(self):
        sorted_values = sorted(self.values.values())
        return sorted_values

if __name__ == '__main__':
    sorter = NumberSorter(5, 2, 8)
    sorted_list = sorter.sort_numbers()
    print(sorted_list)