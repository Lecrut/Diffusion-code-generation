class StringConcatenator:
    def __init__(self, delimiter):
        self.delimiter = delimiter

    def concatenate(self, string_list):
        return self.delimiter.join(string_list)

if __name__ == '__main__':
    sample_strings = ["red", "green", "blue"]
    separator = " | "
    
    concatenator = StringConcatenator(separator)
    
    result1 = concatenator.concatenate(sample_strings)
    print(result1)
    
    additional_strings = ["yellow", "purple"]
    result2 = concatenator.concatenate(additional_strings)
    print(result2)