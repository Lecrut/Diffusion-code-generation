class StringSeparator:

    def separate(self, input_string):
        return '-'.join([char for char in input_string])
if __name__ == '__main__':
    separator = StringSeparator()
    sample_string1 = 'Hello World'
    sample_string2 = 'Python'
    result1 = separator.separate(sample_string1)
    print(result1)
    result2 = separator.separate(sample_string2)
    print(result2)