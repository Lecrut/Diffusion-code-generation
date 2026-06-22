import string

class TextProcessor:
    def __init__(self):
        self.punctuation_set = set(string.punctuation)

    def remove_punctuation(self, text):
        return ''.join(char for char in text if char not in self.punctuation_set)

if __name__ == '__main__':
    processor = TextProcessor()
    
    sample_string1 = "Hello, world! How are you?"
    sample_string2 = "This is a test string with numbers 123 and symbols @#$."
    sample_string3 = "No punctuation here."
    sample_string4 = "!@#$%^&*()_+=-`~[]{}\\|;:'\",.<>/? "

    print(f"'{sample_string1}' -> '{processor.remove_punctuation(sample_string1)}'")
    print(f"'{sample_string2}' -> '{processor.remove_punctuation(sample_string2)}'")
    print(f"'{sample_string3}' -> '{processor.remove_punctuation(sample_string3)}'")
    print(f"'{sample_string4}' -> '{processor.remove_punctuation(sample_string4)}'")