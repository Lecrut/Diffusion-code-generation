class FloatSorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    sorter = FloatSorter([3.5, 1.2, 4.8, 2.1])
    print(sorter.sort())