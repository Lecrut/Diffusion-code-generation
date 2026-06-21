class SubstringChecker:

    def __init__(self, data):
        self.data_set = set(data)

    def check_substring(self, item):
        return item in self.data_set
if __name__ == '__main__':
    checker = SubstringChecker(['apple', 'banana', 'cherry'])
    print(checker.check_substring('banana'))
    print(checker.check_substring('grape'))