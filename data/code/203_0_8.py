class NumberComparer:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def compare(self):
        if self.num1 > self.num2:
            return 'Greater'
        elif self.num1 < self.num2:
            return 'Lesser'
        else:
            return 'Equal'

if __name__ == '__main__':
    comparer = NumberComparer("3.14159", "2.71828")
    result = comparer.compare()
    print(result)