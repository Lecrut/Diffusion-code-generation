class WordFilter:
    def __init__(self):
        self.prefix = None

    def set_prefix(self, prefix):
        self.prefix = prefix.lower()

    def filter_words(self, text):
        if not self.prefix:
            return []
        words = text.lower().split()
        return [word for word in words if word.startswith(self.prefix)]

if __name__ == '__main__':
    sample_text = "This is a sample sentence starting with the letter 't' and another one starting with 's'."
    filter_instance = WordFilter()
    filter_instance.set_prefix('t')
    filtered_words_t = filter_instance.filter_words(sample_text)
    print(filtered_words_t)

    filter_instance.set_prefix('s')
    filtered_words_s = filter_instance.filter_words(sample_text)
    print(filtered_words_s)