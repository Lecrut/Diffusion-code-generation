class NumberSorter:
    @staticmethod
    def compare(a, b):
        return (a > b) - (a < b)

    def sort_three(self, a, b, c):
        if self.compare(a, b) > 0: a, b = b, a
        if self.compare(b, c) > 0: b, c = c, b
        if self.compare(a, b) > 0: a, b = b, a
        return [a, b, c]

if __name__ == '__main__':
    sorter = NumberSorter()
    print(f"Sorting (1, 5, 3): {sorter.sort_three(1, 5, 3)}")
    print(f"Sorting (10, -2, 7): {sorter.sort_three(10, -2, 7)}")