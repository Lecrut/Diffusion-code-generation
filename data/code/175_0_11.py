def separate_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return text.split()

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "Python is fun; let's learn about it... end."
    sample_string3 = "  Multiple   spaces and  punctuation!!! "
    
    print(separate_words(sample_string1))
    print(separate_words(sample_string2))
    print(separate_words(sample_string3))