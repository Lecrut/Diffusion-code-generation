class WordCounter:
    @staticmethod
    def count_words(text):
        if not text.strip():
            return {}
        words = text.split()
        word_count = {}
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence for testing."
    sample_text2 = "Another test case with multiple words."
    sample_text3 = ""
    sample_text4 = "   leading and trailing spaces are handled correctly."

    counter = WordCounter()
    count1 = counter.count_words(sample_text1)
    print(f"Text 1: '{sample_text1}'")
    print(f"Word Count: {count1}\n")

    count2 = counter.count_words(sample_text2)
    print(f"Text 2: '{sample_text2}'")
    print(f"Word Count: {count2}\n")