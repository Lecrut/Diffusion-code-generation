class StringPrefixChecker:
    def __init__(self, valid_prefixes):
        self.valid_prefixes = tuple(valid_prefixes)

    def check(self, strings):
        for s in strings:
            if s.startswith(self.valid_prefixes):
                return True
        return False

if __name__ == '__main__':
    checker = StringPrefixChecker(['A', 'B'])
    sample_data = ['Dog', 'Elephant', 'Ant']
    result = checker.check(sample_data)
    print(result)
    sample_data_2 = ['Cat', 'Bat', 'Dog']
    result_2 = checker.check(sample_data_2)
    print(result_2)