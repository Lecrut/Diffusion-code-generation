class StringSeparator:
    def separate_characters(self, input_string):
        return '-'.join([char for char in input_string])

if __name__ == '__main__':
    separator = StringSeparator()
    sample_string1 = "Hello World"
    result1 = separator.separate_characters(sample_string1)
    print(result1)

    sample_string2 = "Python"
    result2 = separator.separate_characters(sample_string2)
    print(result2)