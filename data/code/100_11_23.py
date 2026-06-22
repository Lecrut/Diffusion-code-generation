class BooleanChecker:
    def __init__(self, data):
        self.data = data

    def all_true(self):
        return all(self.data)

    def all_false(self):
        return not any(self.data)

    def check_uniformity(self):
        if not self.data:
            return True
        first = self.data[0]
        for val in self.data[1:]:
            if val != first:
                return False
        return True

if __name__ == '__main__':
    checker = BooleanChecker([False, False, False])
    print(checker.all_true())
    print(checker.all_false())
    print(checker.check_uniformity())