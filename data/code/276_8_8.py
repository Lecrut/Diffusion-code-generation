class StringRepeater:
    def __init__(self):
        self.U = 3

    @staticmethod
    def repeat_char(char, U):
        return char * U

    def repeat_string(self, text):
        return ''.join(self.repeat_char(char, self.U) for char in text)

if __name__ == '__main__':
    repeater = StringRepeater()
    sample_text = "Hello World"
    repeated_text = repeater.repeat_string(sample_text)
    print(repeated_text)