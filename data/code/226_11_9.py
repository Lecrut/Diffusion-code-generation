class StringRepeater:
    def __init__(self, pattern):
        self.pattern = pattern

    def repeat(self, n):
        return self.pattern * n

if __name__ == '__main__':
    repeater = StringRepeater('AB')
    result = repeater.repeat(1000)
    print(result)