class PairValidator:
    def __init__(self, items):
        self.items = items

    def validate(self):
        if not self.items or len(self.items) < 2:
            raise ValueError("Need at least two items")
        return self.items[0], self.items[-1]

if __name__ == '__main__':
    validator = PairValidator([7, 8, 9, 10])
    print(validator.validate())