class StringWordSplitter:
    @staticmethod
    def split_sentence(text):
        return text.split()

if __name__ == '__main__':
    sample_text = "This is a sample sentence for word splitting."
    words = StringWordSplitter.split_sentence(sample_text)
    print(words)