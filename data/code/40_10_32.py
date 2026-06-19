class StringProcessor:
    @staticmethod
    def get_first_letters(strings):
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_strings = ["kiwi", "mango", "nectarine", "orange", ""]
    result = StringProcessor.get_first_letters(sample_strings)
    print(result)