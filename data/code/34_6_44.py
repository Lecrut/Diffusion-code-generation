class TextFormatter:
    SPACES = ' '

    @staticmethod
    def capitalize_first_letter(s):
        return TextFormatter.SPACES.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    formatter = TextFormatter()
    capitalized_string = TextFormatter.capitalize_first_letter(sample_string)
    print(capitalized_string)