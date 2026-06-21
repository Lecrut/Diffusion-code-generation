class ReverseRangeGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            raise StopIteration
        else:
            current = self.start
            self.start -= 1
            return current

if __name__ == '__main__':
    for number in ReverseRangeGenerator(15, 10):
        print(number)