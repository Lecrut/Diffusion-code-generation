class StringRepeater:
    SEPARATOR = '\n'

    @staticmethod
    def repeat_string(sequence, repetitions):
        return StringRepeater.SEPARATOR.join([sequence] * repetitions)

if __name__ == '__main__':
    repeater = StringRepeater()
    repeated_text = repeater.repeat_string('Hello World', 100)
    print(repeated_text)