def split_text(text):
    return list(filter(None, text.split()))

if __name__ == '__main__':
    sample_text = "  multiple   spaces  between  words  "
    words = split_text(sample_text)
    print(words)