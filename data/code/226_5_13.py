class StringRepeater:
    REPEAT_COUNT = 4

    @staticmethod
    def repeat_string(input_str):
        return input_str * StringRepeater.REPEAT_COUNT

if __name__ == '__main__':
    sample_value = "abc"
    repeated_value = StringRepeater.repeat_string(sample_value)
    print(repeated_value)