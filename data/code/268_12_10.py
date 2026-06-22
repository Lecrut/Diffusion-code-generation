def extract_first_word(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    if not words:
        return ""
    
    return words[0]

if __name__ == '__main__':
    sentence1 = " This is a sample sentence. "
    sentence2 = "\tAnother test case here.\n"
    sentence3 = "singleword"
    empty_sentence = ""
    
    print(extract_first_word(sentence1))
    print(extract_first_word(sentence2))
    print(extract_first_word(sentence3))
    print(extract_first_word(empty_sentence))