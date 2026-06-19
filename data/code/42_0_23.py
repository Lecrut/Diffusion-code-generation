class StringConcatenator:
    def __init__(self, string_list):
        self.string_list = string_list

    def concatenate_with_delimiter(self, delimiter):
        return delimiter.join(self.string_list)

if __name__ == '__main__':
    sample_strings = ["red", "green", "blue"]
    separator = " - "
    
    concat_instance = StringConcatenator(sample_strings)
    result = concat_instance.concatenate_with_delimiter(separator)
    
    print(result)