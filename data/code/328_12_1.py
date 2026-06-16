class StringUtil:
    def get_length(self, text):
        return len(text)
if __name__ == '__main__':
    util = StringUtil()
    sample_string1 = "hello"
    sample_string2 = ""
    sample_string3 = "efficient"
    print(util.get_length(sample_string1))
    print(util.get_length(sample_string2))
    print(util.get_length(sample_string3))