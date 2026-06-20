class StringProcessor:
    def __init__(self, text):
        self.text = text
    
    @staticmethod
    def split_into_words(text):
        return text.split()
    
    def get_first_last_word(self):
        words = self.split_into_words(self.text)
        if len(words) < 2:
            raise ValueError("String must contain at least two words.")
        return words[0], words[-1]

if __name__ == '__main__':
    processor = StringProcessor("This is a sample string for processing")
    try:
        first, last = processor.get_first_last_word()
        print(f"First word: {first}, Last word: {last}")
    except ValueError as e:
        print(f"Error: {e}")