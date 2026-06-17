class StringUtil:
    def get_length(self, text):
        return len(text)
if __name__ == '__main__':
    util = StringUtil()
    sample_string1 = "hello"
    sample_string2 = ""
    sample_string3 = "efficient implementation"
    print(f"Length of '{sample_string1}': {util.get_length(sample_string1)}")
    print(f"Length of '{sample_string2}': {util.get_length(sample_string2)}")
    print(f"Length of '{sample_string3}': {util.get_length(sample_string3)}")