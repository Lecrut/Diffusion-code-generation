class SentenceSplitter:
    def split_sentence(self, text):
        return text.split()

if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_string1 = "  hello world  "
    result1 = splitter.split_sentence(test_string1)
    print(result1)
    
    test_string2 = "multiple   spaces here"
    result2 = splitter.split_sentence(test_string2)
    print(result2)
    
    test_string3 = " leading and trailing "
    result3 = splitter.split_sentence(test_string3)
    print(result3)
    
    test_string4 = ""
    result4 = splitter.split_sentence(test_string4)
    print(result4)