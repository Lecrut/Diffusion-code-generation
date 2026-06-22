class StringProcessor:
    EMPTY_STRING = ""

    @staticmethod
    def get_first_letter(s):
        return s[0] if s else StringProcessor.EMPTY_STRING

if __name__ == '__main__':
    sample_values = ["Hello", "", "World", "Python"]
    results = [StringProcessor.get_first_letter(value) for value in sample_values]
    print(results)