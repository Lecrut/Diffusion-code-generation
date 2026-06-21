def split_sentence(sentence):
    return sentence.split()

if __name__ == '__main__':
    test_string1 = "  hello world  "
    result1 = split_sentence(test_string1)
    print(result1)
    test_string2 = "multiple   spaces here"
    result2 = split_sentence(test_string2)
    print(result2)
    test_string3 = " leading and trailing "
    result3 = split_sentence(test_string3)
    print(result3)
    test_string4 = ""
    result4 = split_sentence(test_string4)
    print(result4)