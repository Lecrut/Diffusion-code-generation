class Summation:
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2
    def add(self):
        return self._value1 + self._value2
if __name__ == '__main__':
    a = 10
    b = 5
    s = Summation(a, b)
    result = s.add()
    print(result)