def keyword_exists(text, keyword):
    return keyword in text

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog."
    sample_keyword = "lazy"
    print(keyword_exists(sample_text, sample_keyword))