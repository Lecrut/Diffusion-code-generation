class StringAnalyzer:
    @staticmethod
    def find_first_word(s):
        index = 0
        while index < len(s) and s[index] != ' ':
            index += 1
        return s[:index]

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string1 = "Hello world"
    sample_string2 = "The quick brown fox"
    sample_string3 = "Jump over the lazy dog"

    print(analyzer.find_first_word(sample_string1))
    print(analyzer.find_first_word(sample_string2))
    print(analyzer.find_first_word(sample_string3))