class NumberSorter:
    def __init__(self, a, b, c):
        self._values = [a, b, c]
    
    @staticmethod
    def _sort_values(values):
        return sorted(values)
    
    def get_sorted_numbers(self):
        return self._sort_values(self._values)

if __name__ == '__main__':
    sorter = NumberSorter(5, 2, 8)
    sorted_list = sorter.get_sorted_numbers()
    print(sorted_list)