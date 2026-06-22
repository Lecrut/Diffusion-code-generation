class ArithmeticProgression:
    def __init__(self, start, difference):
        self.start = start
        self.difference = difference

    def get_nth_term(self, n):
        return self.start + (n - 1) * self.difference

if __name__ == '__main__':
    ap = ArithmeticProgression(3, 4)
    for i in range(1, 16):
        print(ap.get_nth_term(i))