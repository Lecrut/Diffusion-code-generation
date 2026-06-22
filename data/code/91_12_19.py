class BooleanNegator:
    def __init__(self, initial=False):
        self.value = initial

    def set(self, val):
        self.value = val
        return self

    def get(self):
        return self.value

    def negate(self):
        self.value = not self.value
        return self.value

    def __call__(self):
        return not self.value

if __name__ == '__main__':
    negator = BooleanNegator(initial=True)
    result1 = negator.negate()
    negator.set(False)
    result2 = negator()
    print(result1)
    print(result2)