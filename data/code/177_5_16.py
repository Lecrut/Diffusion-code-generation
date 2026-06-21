def split_text_into_words(text):
    return [word for word in text.split(' ') if word]

if __name__ == '__main__':
    sample_text = "  multiple   spaces  between  words  "
    words_list = split_text_into_words(sample_text)
    print(words_list)