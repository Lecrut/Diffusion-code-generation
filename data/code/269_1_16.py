import string

def remove_punctuation(text):
    result = []
    for char in text:
        if char not in string.punctuation:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text1 = "Hello, world! How are you?"
    sample_text2 = "This is a test string with numbers 123 and symbols @#$."
    sample_text3 = "No punctuation here."
    sample_text4 = "!@#$%^&*()_+=-`~[]{}\\|;:'\",.<>/? "
    
    cleaned_text1 = remove_punctuation(sample_text1)
    cleaned_text2 = remove_punctuation(sample_text2)
    cleaned_text3 = remove_punctuation(sample_text3)
    cleaned_text4 = remove_punctuation(sample_text4)
    
    print(f"'{sample_text1}' -> '{cleaned_text1}'")
    print(f"'{sample_text2}' -> '{cleaned_text2}'")
    print(f"'{sample_text3}' -> '{cleaned_text3}'")
    print(f"'{sample_text4}' -> '{cleaned_text4}'")