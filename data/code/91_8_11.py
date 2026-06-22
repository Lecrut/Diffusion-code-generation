class BooleanNegator:
    def __init__(self, initial_value):
        self.value = initial_value

    def get_original(self):
        return self.value

    def negate(self):
        self.value = not self.value
        return self.value

    def reset(self, new_value):
        self.value = new_value
        return self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    original = negator.get_original()
    negated = negator.negate()
    print(f"Original: {original}, Negated: {negated}")

    negator.reset(False)
    original = negator.get_original()
    negated = negator.negate()
    print(f"Original: {original}, Negated: {negated}")