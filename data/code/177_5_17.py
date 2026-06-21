def split_text_into_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = [word.strip() for word in text.split(' ') if word.strip()]
    return words

if __name__ == '__main__':
    sample_text = "  multiple   spaces  between  words  "
    result = split_text_into_words(sample_text)
    print(result)