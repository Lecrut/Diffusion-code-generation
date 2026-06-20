def split_and_trim(s):
    if not s:
        return []
    parts = s.split(',')
    result = [part.strip() for part in parts if part.strip()]
    return result

if __name__ == '__main__':
    test_string = " apple , banana , , cherry ,  date  ,  , fig "
    print(split_and_trim(test_string))
    empty_string = ""
    print(split_and_trim(empty_string))
    whitespace_string = "   ,  ,  "
    print(split_and_trim(whitespace_string))
    normal_string = "a,b,c"
    print(split_and_trim(normal_string))