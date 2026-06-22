class ReverseRangeGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def generate(self):
        current = self.start - 1
        while current >= self.stop:
            yield current
            current -= 1

if __name__ == '__main__':
    generator = ReverseRangeGenerator(25, 20)
    for number in generator.generate():
        print(number)