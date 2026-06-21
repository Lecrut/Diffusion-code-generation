def keyword_exists(text, keyword):
    return keyword in text

if __name__ == '__main__':
    test_text = "Python is a high-level, interpreted programming language."
    test_keyword = "interpreted"
    print(keyword_exists(test_text, test_keyword))