class IndexProcessor:
    def __init__(self):
        self.indices = []
        self.squares = []

    def process_index(self, index):
        self.indices.append(index)
        self.squares.append(index ** 2)

    def get_results(self):
        return self.indices, self.squares

if __name__ == '__main__':
    processor = IndexProcessor()
    for i in range(5):
        processor.process_index(i)
    indices, squares = processor.get_results()
    print("Indices:", indices)
    print("Squares:", squares)