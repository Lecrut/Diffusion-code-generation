class NumberFinder:
    def __init__(self):
        self.numbers = {}

    def add_number(self, key, value):
        if key not in self.numbers or value > self.numbers[key]:
            self.numbers[key] = value

    def get_maximum(self):
        return max(self.numbers.values()) if self.numbers else None

if __name__ == '__main__':
    finder = NumberFinder()
    finder.add_number("key1", 10)
    finder.add_number("key2", 20)
    finder.add_number("key3", 30)
    finder.add_number("key4", 40)
    finder.add_number("key5", 50)
    print(f"Maximum number: {finder.get_maximum()}")