class SubstringSearcher:
    @staticmethod
    def word_present(target_word, text):
        words = set(text.split())
        return target_word in words

if __name__ == '__main__':
    searcher = SubstringSearcher()
    target1 = "python"
    text1 = "This is a sample text about python programming."
    text2 = "This text does not contain the word python."
    text3 = "Python is fun."
    text4 = "programming"

    print(f"'{target1}' in '{text1}': {searcher.word_present(target1, text1)}")
    print(f"'{target1}' in '{text2}': {searcher.word_present(target1, text2)}")
    print(f"'{target1}' in '{text3}': {searcher.word_present(target1, text3)}")
    print(f"'{target1}' in '{text4}': {searcher.word_present(target1, text4)}")