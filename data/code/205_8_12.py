class NumberSorter:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        if isinstance(number, str):
            number = float(number)
        self.numbers.append(number)

    def sort_numbers(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    sorter = NumberSorter()
    sorter.add_number('3.5')
    sorter.add_number(2)
    sorter.add_number('4')
    sorter.add_number(1.1)
    print(sorter.sort_numbers())