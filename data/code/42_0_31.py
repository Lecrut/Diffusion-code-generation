class StringConcatenator:

    def __init__(self, string_list, delimiter):
        self.string_list = string_list
        self.delimiter = delimiter

    def concatenate(self):
        return self.delimiter.join(self.string_list)
if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry']
    separator = ', '
    concatenator = StringConcatenator(sample_strings, separator)
    result1 = concatenator.concatenate()
    print(result1)
    concatenator.string_list.append('date')
    result2 = concatenator.concatenate()
    print(result2)