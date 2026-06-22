class NumberHandler:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_extremes(self):
        return (min(self.numbers), max(self.numbers)) if self.numbers else None

if __name__ == '__main__':
    handler = NumberHandler([3, 1, 4, 1, 5, 9])
    print(handler.get_extremes())
    handler = NumberHandler([])
    print(handler.get_extremes())