def keyword_exists(text, keyword):
    return keyword in text

if __name__ == '__main__':
    search_text = "Python is an interpreted, high-level and general-purpose programming language."
    search_keyword = "interpreted"
    result = keyword_exists(search_text, search_keyword)
    print(result)