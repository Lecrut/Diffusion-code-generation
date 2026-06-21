def split_text_to_words(text):
    return [word for word in text.split() if word]

if __name__ == '__main__':
    sample_text = "  multiple   spaces  between  words  "
    words = split_text_to_words(sample_text)
    print(words)