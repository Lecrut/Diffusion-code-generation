class Subtractor:
    def __init__(self, first_value, second_value):
        self.first = first_value
        self.second = second_value
    def subtract(self):
        return self.first - self.second
if __name__ == '__main__':
    a = 20
    b = 7
    sub = Subtractor(a, b)
    result = sub.subtract()
    print(result)