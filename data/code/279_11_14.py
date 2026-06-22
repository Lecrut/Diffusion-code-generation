class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    @staticmethod
    def create(lst):
        return ReverseIterator(lst)

    def next(self):
        if self.index > 0:
            self.index -= 1
            return self.lst[self.index]
        else:
            raise StopIteration

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    iterator = ReverseIterator.create(sample_values)
    while True:
        try:
            print(iterator.next())
        except StopIteration:
            break