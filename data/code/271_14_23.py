import re

class StringModifier:
    def __init__(self):
        self.vowels = 'aeiouAEIOU'
    
    def remove_vowels(self, text):
        pattern = f"[{re.escape(self.vowels)}]"
        return re.sub(pattern, '', text)

if __name__ == '__main__':
    modifier = StringModifier()
    sample_text = "Hello, World!"
    print(modifier.remove_vowels(sample_text))