class EvenZeroGenerator:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate(self):
        for num in range(self.start, self.end + 1):
            if num % 2 == 0:
                yield (True if num == 0 else False)
if __name__ == '__main__':
    generator = EvenZeroGenerator(-5, 5)
    for result in generator.generate():
        print(result)
    another_generator = EvenZeroGenerator(0, 10)
    for result in another_generator.generate():
        print(result)