def validate_input(text, keyword):
    if not isinstance(text, str) or not isinstance(keyword, str):
        raise ValueError("Both text and keyword must be strings")

def keyword_exists(text, keyword):
    validate_input(text, keyword)
    return keyword in text

if __name__ == '__main__':
    sample_text = "Python is a high-level, interpreted programming language."
    sample_keyword = "interpreted"
    print(keyword_exists(sample_text, sample_keyword))