import re

class TextProcessor:
    def __init__(self):
        self.vowels = 'aeiouAEIOU'
    
    def remove_vowels(self, text):
        pattern = f"[{re.escape(self.vowels)}]"
        return re.sub(pattern, '', text)

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text1 = "Hello, World!"
    print(processor.remove_vowels(sample_text1))
    
    sample_text2 = "Python Programming"
    print(processor.remove_vowels(sample_text2))