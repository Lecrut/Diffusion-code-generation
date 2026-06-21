class EvenZeroGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate(self):
        for num in range(self.start, self.end + 1):
            if num % 2 == 0:
                yield num == 0

if __name__ == '__main__':
    generator = EvenZeroGenerator(-3, 7)
    for result in generator.generate():
        print(result)