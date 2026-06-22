class TriangularSequence:
    def __init__(self):
        self.sequence = []

    def generate(self, n):
        self.sequence = [sum(range(1, i+1)) for i in range(1, n+1)]
        return self.sequence

if __name__ == '__main__':
    ts = TriangularSequence()
    print(ts.generate(12))