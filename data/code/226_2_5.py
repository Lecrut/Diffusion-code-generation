class StringRepeater:
    def repeat_string(self, string, repetitions):
        return [string] * repetitions

if __name__ == '__main__':
    repeater = StringRepeater()
    sample_string = 'Hello World'
    sample_repetitions = 100
    repeated_strings = repeater.repeat_string(sample_string, sample_repetitions)
    result = '\n'.join(repeated_strings)
    print(result)