class Subtractor:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def subtract(self):
        return self.first - self.second
if __name__ == '__main__':
    a = 20
    b = 7
    sub = Subtractor(a, b)
    result = sub.subtract()
    print(result)