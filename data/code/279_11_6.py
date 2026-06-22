class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = self.lst[self.index]
        self.index -= 1
        return result

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    reverse_iter = ReverseIterator(sample_values)
    for value in reverse_iter:
        print(value)