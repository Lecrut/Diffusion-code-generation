class NumberCalculator:
    def __init__(self, data):
        self.data = data

    def get_count(self):
        return len(self.data)

    def get_total(self):
        return sum(self.data)

    def get_average(self):
        if not self.data:
            return 0
        return self.get_total() / self.get_count()

if __name__ == '__main__':
    static_list = [5, 15, 25, 35, 45]
    calculator = NumberCalculator(static_list)
    print(calculator.get_average())