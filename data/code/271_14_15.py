import re

class TextFilter:
    VOWELS = 'aeiouAEIOU'
    
    @staticmethod
    def remove_vowels(text):
        pattern = f"[{re.escape(TextFilter.VOWELS)}]"
        return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    filtered_text = TextFilter.remove_vowels(sample_text)
    print(filtered_text)