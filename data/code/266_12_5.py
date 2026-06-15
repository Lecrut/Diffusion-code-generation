class WordCounter:
    def count_words(self, text):
        words = text.split()
        return len(words)
if __name__ == '__main__':
    sample_text1 = "This is a sample sentence for testing."
    sample_text2 = "Another test case with multiple words."
    sample_text3 = "   leading and trailing spaces test  "
    counter = WordCounter()
    count1 = counter.count_words(sample_text1)
    print(f"Text: '{sample_text1}'")
    print(f"Word count: {count1}\n")
    count2 = counter.count_words(sample_text2)
    print(f"Text: '{sample_text2}'")
    print(f"Word count: {count2}\n")
    count3 = counter.count_words(sample_text3)
    print(f"Text: '{sample_text3}'")
    print(f"Word count: {count3}")