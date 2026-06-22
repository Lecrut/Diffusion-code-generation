class StringRepeater:
    def repeat_string(self, string, repetitions):
        result = [string] * repetitions
        return '\n'.join(result)

if __name__ == '__main__':
    repeater = StringRepeater()
    sample_string = 'Hello World'
    sample_repetitions = 100
    repeated_result = repeater.repeat_string(sample_string, sample_repetitions)
    print(repeated_result)