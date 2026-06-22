class BothFalseChecker:
    def __init__(self, val_a, val_b):
        self.val_a = val_a
        self.val_b = val_b

    def check(self):
        return self.val_a is False and self.val_b is False

def both_false_generator(a, b):
    checker = BothFalseChecker(a, b)
    yield checker.check()

if __name__ == '__main__':
    results = []
    for pair in [(False, False), (True, False), (False, True), (True, True)]:
        gen = both_false_generator(pair[0], pair[1])
        results.append(next(gen))
    print(results)