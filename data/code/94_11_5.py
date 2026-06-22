def check_any_true(values):
    if not values:
        return False
    return any(values)

class BooleanChecker:
    def __init__(self, data):
        self.data = data

    def has_true(self):
        return any(self.data)

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    result = check_any_true(sample_data)
    print(result)
    
    checker = BooleanChecker([False, False, False])
    print(checker.has_true())
    
    checker_true = BooleanChecker([True, False])
    print(checker_true.has_true())