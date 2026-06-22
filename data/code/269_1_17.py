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
    
    result1 = processor.remove_punctuation(sample_string1)
    result2 = processor.remove_punctuation(sample_string2)
    result3 = processor.remove_punctuation(sample_string3)
    result4 = processor.remove_punctuation(sample_string4)
    
    print(f"'{sample_string1}' -> '{result1}'")
    print(f"'{sample_string2}' -> '{result2}'")
    print(f"'{sample_string3}' -> '{result3}'")
    print(f"'{sample_string4}' -> '{result4}'")