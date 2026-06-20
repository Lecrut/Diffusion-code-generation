class BothFalseGenerator:
    @staticmethod
    def generate(a: bool, b: bool):
        if not a and not b:
            yield True

if __name__ == '__main__':
    gen = BothFalseGenerator.generate(False, False)
    print(next(gen))
    gen = BothFalseGenerator.generate(True, False)
    print(next(gen))