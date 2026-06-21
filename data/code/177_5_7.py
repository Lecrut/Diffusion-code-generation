def split_text(text):
    return [word for word in text.split() if word]

if __name__ == '__main__':
    sample_text = '  multiple   spaces  between  words  '
    result = split_text(sample_text)
    print(result)