class StringManipulator:
    @staticmethod
    def capitalize_first_letter(s):
        return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_string = "this is another test string"
    result = StringManipulator.capitalize_first_letter(sample_string)
    print(result)