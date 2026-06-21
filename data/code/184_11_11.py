def keyword_exists(text, keyword):
    return keyword in text

if __name__ == '__main__':
    sample_text = "Hello, world!"
    sample_keyword = "world"
    print(keyword_exists(sample_text, sample_keyword))