class ArithmeticProgression:
    def __init__(self, start, difference):
        self.start = start
        self.difference = difference

    def get_term(self, index):
        return self.start + index * self.difference

if __name__ == '__main__':
    ap = ArithmeticProgression(3, 4)
    for i in range(15):
        print(ap.get_term(i))