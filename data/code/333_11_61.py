class StringProcessor:
    def get_first_chars(self, s):
        return ''.join(word[0] for word in s.split())
if __name__ == '__main__':
    sp = StringProcessor()
    test_input = "Hello world this is a sample string"
    result = sp.get_first_chars(test_input)
    print(result)