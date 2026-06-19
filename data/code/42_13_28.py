class StringConcatenator:
    def __init__(self, separator):
        self.separator = separator

    def concatenate(self, string_list):
        if not all(isinstance(s, str) for s in string_list):
            raise TypeError("All elements must be strings")
        return ''.join(string_list)

if __name__ == '__main__':
    sample_values1 = ["Hello", " ", "World", "!"]
    sample_values2 = ["Python", "is", "awesome"]
    separator = ", "

    concatenator = StringConcatenator(separator)
    
    try:
        result1 = concatenator.concatenate(sample_values1)
        print(result1)
    except TypeError as e:
        print(e)

    try:
        result2 = concatenator.concatenate(sample_values2)
        print(result2)
    except TypeError as e:
        print(e)