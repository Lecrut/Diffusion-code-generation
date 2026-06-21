SAMPLE_TEXT = 'This is a sample text for testing.'
SAMPLE_KEYWORD = 'sample'

def keyword_exists(text, keyword):
    return keyword in text
if __name__ == '__main__':
    result = keyword_exists(SAMPLE_TEXT, SAMPLE_KEYWORD)
    print(result)