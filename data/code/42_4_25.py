class StringConcatenator:
    def __init__(self, iterable, separator):
        self.iterable = iterable
        self.separator = separator

    def concatenate_segments(self):
        for segment in self.iterable:
            yield segment
            yield self.separator

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = " - "
    
    concatenator = StringConcatenator(sample_strings, custom_separator)
    result_generator = concatenator.concatenate_segments()
    
    final_string = ""
    for item in result_generator:
        final_string += item
    
    print(final_string.rstrip(custom_separator))