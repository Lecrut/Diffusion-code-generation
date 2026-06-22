class Rhombus:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.area = 0.5 * d1 * d2

if __name__ == '__main__':
    r = Rhombus(6.0, 8.0)
    print(r.area)
    print(r.d1 * r.d2 / 2.0)