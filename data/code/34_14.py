def title_case(s):
    return ' '.join(word.capitalize() for word in s.split())
if __name__ == '__main__':
    test_string = "this is a sample string for title casing"
    result = title_case(test_string)
    print(result)