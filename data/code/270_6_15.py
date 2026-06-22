class StringManipulator:
    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(' ', '')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "   this has spaces   ",
        "no_spaces"
    ]
    
    for string in sample_strings:
        result = StringManipulator.remove_spaces(string)
        print(result)