class ValueSorter:
    def __init__(self, values):
        self.values = sorted(values)

    def get_middle_value(self):
        return self.values[1]

if __name__ == '__main__':
    sorter = ValueSorter([5, 2, 8])
    print(sorter.get_middle_value())