MAX_SPACES = 100

def split_text_into_words(text):
    return [word.strip() for word in text.split(' ') if word.strip()]

if __name__ == '__main__':
    long_string = "  multiple   spaces  between  words  "
    result = split_text_into_words(long_string)
    print(result)