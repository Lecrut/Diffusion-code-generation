class WordFrequencyCounter:
    @staticmethod
    def count_words(text):
        if not text.strip():
            return {}
        words = text.split()
        word_count = {}
        for word in words:
            word = word.strip(".,!?;:")
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        return word_count

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence. For testing."
    sample_text2 = "Another test case with multiple words!"
    sample_text3 = ""
    sample_text4 = "   leading and trailing spaces are handled correctly."

    counter = WordFrequencyCounter()
    freq1 = counter.count_words(sample_text1)
    print(f"Text 1: '{sample_text1}'")
    print("Word Frequencies:", freq1, "\n")

    freq2 = counter.count_words(sample_text2)
    print(f"Text 2: '{sample_text2}'")
    print("Word Frequencies:", freq2, "\n")