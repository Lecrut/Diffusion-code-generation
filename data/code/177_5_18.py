class TextSplitter:
    @staticmethod
    def split_text(text):
        return [word.strip() for word in text.split(' ') if word.strip()]

if __name__ == '__main__':
    sample_text = "  multiple   spaces  between  words  "
    words = TextSplitter.split_text(sample_text)
    print(words)