def get_first_word(text):
    words = text.split()
    if words:
        return words[0]
    else:
        return ""

if __name__ == '__main__':
    sample_text1 = "Hello world"
    sample_text2 = "   leading spaces and multiple words"
    sample_text3 = ""
    
    print(get_first_word(sample_text1))
    print(get_first_word(sample_text2))
    print(get_first_word(sample_text3))