class StringRepeater:
    def __init__(self, strings):
        self.strings = strings

    @staticmethod
    def repeat_string(s, M):
        return s * M

    def repeat_all(self, M):
        return [self.repeat_string(s, M) for s in self.strings]

if __name__ == '__main__':
    sample_strings = ["hello", "world"]
    M = 3
    repeater = StringRepeater(sample_strings)
    result = repeater.repeat_all(M)
    print(result)