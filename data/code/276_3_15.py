class StringRepeater:
    def __init__(self, string):
        self.string = string

    def repeat(self, P):
        return self.string * P

if __name__ == '__main__':
    repeater = StringRepeater("abc")
    print(repeater.repeat(3))
    print(repeater.repeat(5))