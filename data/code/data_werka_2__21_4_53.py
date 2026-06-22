class ReverseRangeGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            result = self.start
            self.start -= 1
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    generator = ReverseRangeGenerator(20, 15)
    for number in generator:
        print(number)