import string

class PunctuationRemover:
    PUNCTUATION_CHARS = set(string.punctuation)

    @staticmethod
    def remove_punctuation(text):
        return ''.join(char for char in text if char not in PunctuationRemover.PUNCTUATION_CHARS)

if __name__ == '__main__':
    remover = PunctuationRemover()
    sample_string1 = "Hello, world! How are you?"
    sample_string2 = "This is a test string with numbers 123 and symbols @#$."
    sample_string3 = "No punctuation here."
    sample_string4 = "!@#$%^&*()_+=-`~[]{}\\|;:'\",.<>/? "
    
    result1 = remover.remove_punctuation(sample_string1)
    result2 = remover.remove_punctuation(sample_string2)
    result3 = remover.remove_punctuation(sample_string3)
    result4 = remover.remove_punctuation(sample_string4)
    
    print(f"'{sample_string1}' -> '{result1}'")
    print(f"'{sample_string2}' -> '{result2}'")
    print(f"'{sample_string3}' -> '{result3}'")
    print(f"'{sample_string4}' -> '{result4}'")