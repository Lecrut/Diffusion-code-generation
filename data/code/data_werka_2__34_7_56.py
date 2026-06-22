class StringCapitalizer:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        self.input_string = input_string

    def capitalize(self):
        words = self.input_string.split()
        capitalized_words = [word[0].upper() + word[1:] for word in words]
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "this is a test with different casing."
    try:
        capitalizer = StringCapitalizer(sample_input)
        result = capitalizer.capitalize()
        print(result)
    except ValueError as e:
        print(e)