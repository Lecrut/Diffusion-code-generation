class ListProcessor:
    def __init__(self):
        self.indices = []
        self.squares = []

    def process(self, count):
        for i in range(count):
            self.indices.append(i)
            self.squares.append(i ** 2)

if __name__ == '__main__':
    processor = ListProcessor()
    processor.process(5)
    print("Indices:", processor.indices)
    print("Squares:", processor.squares)