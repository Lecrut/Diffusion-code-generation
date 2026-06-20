class BoolChecker:
    def both_false_generator(self, a: bool, b: bool):
        if not a and not b:
            yield True

if __name__ == '__main__':
    checker = BoolChecker()
    gen1 = checker.both_false_generator(False, False)
    print(next(gen1))
    gen2 = checker.both_false_generator(True, False)
    print(next(gen2))
    gen3 = checker.both_false_generator(False, True)
    print(next(gen3))
    gen4 = checker.both_false_generator(True, True)
    print(next(gen4))