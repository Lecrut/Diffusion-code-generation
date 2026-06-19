class StringConcatenator:
    def __init__(self, string_list, delimiter):
        if not all(isinstance(s, str) for s in string_list):
            raise ValueError("All elements in the string list must be strings.")
        if not isinstance(delimiter, str):
            raise ValueError("Delimiter must be a string.")
        
        self.string_list = string_list
        self.delimiter = delimiter

    def concatenate(self):
        return self.delimiter.join(self.string_list)

if __name__ == '__main__':
    sample_strings = ["alpha", "beta", "gamma"]
    separator = " - "
    try:
        concat_instance = StringConcatenator(sample_strings, separator)
        result = concat_instance.concatenate()
        print(result)
    except ValueError as e:
        print(e)