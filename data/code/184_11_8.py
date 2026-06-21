def keyword_exists(text, keyword):
    return keyword in text

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string."
    sample_keyword = "test"
    result = keyword_exists(sample_text, sample_keyword)
    print(result)