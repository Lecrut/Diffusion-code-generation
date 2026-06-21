def find_opposite_truth(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    if value:
        return False
    return True

if __name__ == '__main__':
    class TruthChecker:
        def __init__(self):
            self.results = []
        def check(self, val):
            result = find_opposite_truth(val)
            self.results.append(result)
            return result
    
    checker = TruthChecker()
    print(checker.check(True))
    print(checker.check(False))
    print(checker.check(True))
    print(checker.check(False))