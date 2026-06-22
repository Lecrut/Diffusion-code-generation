class StarSquare:
    SIZE = 4
    CHARACTER = '*'

    @staticmethod
    def create_row():
        return StarSquare.CHARACTER * StarSquare.SIZE

    @staticmethod
    def generate():
        return [StarSquare.create_row() for _ in range(StarSquare.SIZE)]

if __name__ == '__main__':
    result = StarSquare.generate()
    for line in result:
        print(line)