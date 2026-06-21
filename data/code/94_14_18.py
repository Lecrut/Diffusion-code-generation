class BooleanChecker:
    def __init__(self, data):
        self.data = list(data)

    def has_true(self):
        index = 0
        length = len(self.data)
        while index < length:
            if self.data[index]:
                return True
            index += 1
        return False

    def count_trues(self):
        total = 0
        for val in self.data:
            if val:
                total += 1
        return total

if __name__ == '__main__':
    checker = BooleanChecker([False, False, False])
    print(checker.has_true())
    print(checker.count_trues())
    
    checker2 = BooleanChecker([False, True, False])
    print(checker2.has_true())
    print(checker2.count_trues())