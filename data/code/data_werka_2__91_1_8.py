class BooleanNegator:
    def __init__(self):
        self.value = None

    def negate(self, flag: bool) -> bool:
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        self.value = not flag
        return self.value

if __name__ == '__main__':
    negator = BooleanNegator()
    result = negator.negate(True)
    print(result)
    result2 = negator.negate(False)
    print(result2)