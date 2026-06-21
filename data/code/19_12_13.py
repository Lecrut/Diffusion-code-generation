import random

class StringSelector:
    def __init__(self, data):
        self.data = data

    def select(self, seed_value):
        random.seed(seed_value)
        index = random.randint(0, len(self.data) - 1)
        return self.data[index]

if __name__ == '__main__':
    items = ("red", "blue", "green", "yellow", "purple")
    selector = StringSelector(items)
    result_first = selector.select(123)
    result_second = selector.select(456)
    print(result_first)
    print(result_second)