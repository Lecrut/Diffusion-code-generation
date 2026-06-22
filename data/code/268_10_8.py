class WordFinder:
    def find_first_word(self, s):
        index = 0
        while index < len(s) and s[index] != ' ':
            index += 1
        return s[:index]

if __name__ == '__main__':
    finder = WordFinder()
    print(finder.find_first_word("Hello world"))
    print(finder.find_first_word("The quick brown fox"))
    print(finder.find_first_word("Jump over the lazy dog"))
    print(finder.find_first_word("Lazy dogs jump over the lazy fox"))