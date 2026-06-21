class NumberSorter:
    def sort(self, a, b):
        if a < b:
            return a, b
        return b, a

if __name__ == '__main__':
    sorter = NumberSorter()
    pair_one = sorter.sort(42, 17)
    print(pair_one)
    pair_two = sorter.sort(99, 101)
    print(pair_two)
    pair_three = sorter.sort(5, 5)
    print(pair_three)