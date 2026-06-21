class StringCapitalizer:
    @staticmethod
    def capitalize_first_letter(word):
        return word[0].upper() + word[1:]

    def __init__(self, input_string):
        self.input_string = input_string

    def process(self):
        words = self.input_string.split()
        capitalized_words = [StringCapitalizer.capitalize_first_letter(word) for word in words]
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "exploring the vast universe of technology"
    capitalizer = StringCapitalizer(sample_string)
    result = capitalizer.process()
    print(result)