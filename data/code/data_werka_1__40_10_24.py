class StringProcessor:
    @staticmethod
    def get_first_letters(string_list):
        return [s[0] for s in string_list if s]

if __name__ == '__main__':
    sample_strings = ["kiwi", "mango", "nectarine", "orange", ""]
    result = StringProcessor.get_first_letters(sample_strings)
    print(result)