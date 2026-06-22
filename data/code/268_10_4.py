class StringProcessor:
    @staticmethod
    def find_first_word(s):
        index = 0
        while index < len(s) and s[index] != ' ':
            index += 1
        return s[:index]

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Lazy dogs jump over the lazy fox"
    print(processor.find_first_word(sample_string))