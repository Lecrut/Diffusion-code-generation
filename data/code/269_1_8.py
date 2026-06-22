import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

if __name__ == '__main__':
    sample_text1 = "Hello, world! How are you?"
    sample_text2 = "This is a test string with numbers 123 and symbols @#$."
    sample_text3 = "No punctuation here."
    sample_text4 = "!@#$%^&*()_+=-`~[]{}\\|;:'\",.<>/? "
    
    result1 = remove_punctuation(sample_text1)
    result2 = remove_punctuation(sample_text2)
    result3 = remove_punctuation(sample_text3)
    result4 = remove_punctuation(sample_text4)
    
    print(f"'{sample_text1}' -> '{result1}'")
    print(f"'{sample_text2}' -> '{result2}'")
    print(f"'{sample_text3}' -> '{result3}'")
    print(f"'{sample_text4}' -> '{result4}'")