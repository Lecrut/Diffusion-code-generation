def get_first_word(text):
    words = text.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_text_1 = "Hello world"
    sample_text_2 = "   leading spaces and multiple words"
    sample_text_3 = ""
    
    print(get_first_word(sample_text_1))
    print(get_first_word(sample_text_2))
    print(get_first_word(sample_text_3))