def keyword_exists(text, keyword):
    return keyword in text

if __name__ == '__main__':
    test_text = "Data structures and algorithms are fundamental to computer science."
    search_keyword = "algorithms"
    result = keyword_exists(test_text, search_keyword)
    print(result)