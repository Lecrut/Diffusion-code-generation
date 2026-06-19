class NumericComparer:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def are_inequal(self):
        return self.value1 != self.value2

if __name__ == '__main__':
    comparer = NumericComparer(5, 10)
    result = comparer.are_inequal()
    print(result)