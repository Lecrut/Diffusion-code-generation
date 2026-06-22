class BooleanNegator:
    def __init__(self, value):
        self.original = value

    def get_negated(self):
        return not self.original

    def get_state(self):
        return {
            "original": self.original,
            "negated": self.get_negated()
        }

if __name__ == '__main__':
    values = [True, False]
    for v in values:
        negator = BooleanNegator(v)
        state = negator.get_state()
        print(f"Original: {state['original']}")
        print(f"Negated: {state['negated']}")
        print("---")