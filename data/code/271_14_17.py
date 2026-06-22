import re

class TextCleaner:
    def __init__(self):
        self.vowels = 'aeiouAEIOU'
    
    def remove_vowels(self, text):
        pattern = f"[{re.escape(self.vowels)}]"
        return re.sub(pattern, '', text)

if __name__ == '__main__':
    cleaner = TextCleaner()
    sample_text = "Hello, World!"
    print(cleaner.remove_vowels(sample_text))