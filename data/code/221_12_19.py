class NumberSorter:
    def __init__(self, a, b, c):
        if not all(isinstance(i, (int, float)) for i in [a, b, c]):
            raise ValueError("All inputs must be numbers")
        self.numbers = sorted([a, b, c])

    def get_sorted_numbers(self):
        return self.numbers

if __name__ == '__main__':
    sorter = NumberSorter(5.1, 2, 8)
    sorted_list = sorter.get_sorted_numbers()
    print(sorted_list)