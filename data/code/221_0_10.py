class Sorter:
    def __init__(self):
        self.swapped = True

    @staticmethod
    def swap(a, b):
        return b, a

    def sort_numbers(self, a, b, c):
        while self.swapped:
            self.swapped = False
            if a > b:
                a, b = self.swap(a, b)
                self.swapped = True
            if b > c:
                b, c = self.swap(b, c)
                self.swapped = True
        return a, b, c

if __name__ == '__main__':
    sorter = Sorter()
    result = sorter.sort_numbers(3, 1, 2)
    print(result)