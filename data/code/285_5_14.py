class AscDescChecker:
    def __init__(self, input_string):
        self.input_string = input_string

    def check_pairs(self):
        result = []
        for i in range(len(self.input_string) - 1):
            if ord(self.input_string[i]) < ord(self.input_string[i + 1]):
                result.append('ascending')
            elif ord(self.input_string[i]) > ord(self.input_string[i + 1]):
                result.append('descending')
            else:
                result.append('equal')
        return result

if __name__ == '__main__':
    checker = AscDescChecker("abcde")
    print(checker.check_pairs())

    checker = AscDescChecker("edcba")
    print(checker.check_pairs())