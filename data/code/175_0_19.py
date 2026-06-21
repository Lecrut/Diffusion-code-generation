def separate_words(text):
    return text.split()

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "Python is fun; let's learn about it... end."
    sample_string3 = "  Multiple   spaces and  punctuation!!! "
    
    print(f"Input: '{sample_string1}'")
    print(f"Output: {separate_words(sample_string1)}")
    
    print(f"Input: '{sample_string2}'")
    print(f"Output: {separate_words(sample_string2)}")
    
    print(f"Input: '{sample_string3}'")
    print(f"Output: {separate_words(sample_string3)}")