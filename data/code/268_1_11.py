def get_first_word(text):
    words = text.split()
    if words:
        return words[0]
    return ""

if __name__ == '__main__':
    sample_texts = [
        "Hello world",
        "   leading spaces and multiple words",
        "",
        "singleword",
        "",
        ""
    ]
    
    for text in sample_texts:
        print(get_first_word(text))