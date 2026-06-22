class StringRepeater:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    @staticmethod
    def repeat_string(s, M):
        return s * M

    def repeat_strings(self, strings):
        return [self.repeat_string(s, self.multiplier) for s in strings]

if __name__ == '__main__':
    repeater = StringRepeater(3)
    sample_strings = ["hello", "world"]
    result = repeater.repeat_strings(sample_strings)
    print(result)