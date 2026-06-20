class GreaterThanTen:
    def __init__(self):
        self.value1 = 5
        self.value2 = 12

    def check_or_condition(self):
        return self.value1 > 10 or self.value2 > 10

if __name__ == '__main__':
    instance = GreaterThanTen()
    result = instance.check_or_condition()
    print(result)