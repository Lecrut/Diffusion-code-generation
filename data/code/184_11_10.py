SEARCH_KEYWORD = "sample"

def keyword_exists(text, keyword=SEARCH_KEYWORD):
    return keyword in text

if __name__ == '__main__':
    sample_text = "This is a sample text for testing."
    print(keyword_exists(sample_text))