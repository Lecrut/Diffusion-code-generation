class StringConcatenator:
    def __init__(self, string_list, delimiter):
        if not all(isinstance(s, str) for s in string_list):
            raise ValueError("All elements in the string list must be strings.")
        if not isinstance(delimiter, str):
            raise TypeError("Delimiter must be a string.")
        
        self.string_list = string_list
        self.delimiter = delimiter

    def concatenate(self):
        return self.delimiter.join(self.string_list)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    separator = ", "
    
    try:
        concatenator = StringConcatenator(sample_strings, separator)
        result = concatenator.concatenate()
        print(result)
    except (ValueError, TypeError) as e:
        print(e)