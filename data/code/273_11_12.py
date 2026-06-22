class IndexProcessor:
    def __init__(self):
        self.indices = []
        self.squares = []

    def process(self, count=5):
        for i in range(count):
            self.indices.append(i)
            self.squares.append(i ** 2)

if __name__ == '__main__':
    processor = IndexProcessor()
    processor.process()
    print("Indices:", processor.indices)
    print("Squares:", processor.squares)