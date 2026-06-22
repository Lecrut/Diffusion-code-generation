class WordCounter:
    @staticmethod
    def count_words(text):
        return len(text.split())

if __name__ == '__main__':
    test_string1 = "This is a sample sentence."
    test_string2 = "  Multiple   spaces here."
    test_string3 = ""
    test_string4 = "SingleWord"
    print(f"'{test_string1}': {WordCounter.count_words(test_string1)}")
    print(f"'{test_string2}': {WordCounter.count_words(test_string2)}")
    print(f"'{test_string3}': {WordCounter.count_words(test_string3)}")
    print(f"'{test_string4}': {WordCounter.count_words(test_string4)}")