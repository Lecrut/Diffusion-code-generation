def validate_inputs(text, keyword):
    if not isinstance(text, str) or not isinstance(keyword, str):
        raise ValueError("Both text and keyword must be strings")

def keyword_exists(text, keyword):
    validate_inputs(text, keyword)
    return keyword in text

if __name__ == '__main__':
    sample_text = "This is a sample text for testing."
    sample_keyword = "sample"
    print(keyword_exists(sample_text, sample_keyword))