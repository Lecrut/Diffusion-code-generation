def get_first_word(text):
    words = text.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_texts = [
        "Hello world",
        "   leading spaces and multiple words",
        "",
        "singleword",
        "  "
    ]
    
    for text in sample_texts:
        print(f"Input: '{text}', Output: '{get_first_word(text)}'")