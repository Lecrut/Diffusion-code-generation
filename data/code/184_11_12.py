def keyword_exists(text, keyword):
    return keyword in text

if __name__ == '__main__':
    sample_text = "This is a sample text for testing."
    search_keyword = "sample"
    print(keyword_exists(sample_text, search_keyword))