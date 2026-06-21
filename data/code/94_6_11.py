class BooleanChecker:
    def __init__(self, data):
        self.data = data
        self.cache = False
        self.checked = False

    def has_true(self):
        if self.checked:
            return self.cache
        result = False
        for element in self.data:
            if element:
                result = True
                break
        self.cache = result
        self.checked = True
        return result

    def count_true(self):
        count = 0
        for element in self.data:
            if element:
                count += 1
        return count

if __name__ == '__main__':
    sample_data = [False, False, False, True, False]
    sample_empty = []
    checker = BooleanChecker(sample_data)
    print(checker.has_true())
    print(checker.count_true())
    empty_checker = BooleanChecker(sample_empty)
    print(empty_checker.has_true())
    print(empty_checker.count_true())