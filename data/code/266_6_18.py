class WordCounter:
    def count_words_starting_with(self, text, letter):
        if not text:
            return 0
        words = text.split()
        return sum(word.startswith(letter) for word in words)

if __name__ == '__main__':
    counter = WordCounter()
    sample_text = "apple banana applebee apricot"
    print(counter.count_words_starting_with(sample_text, 'a'))