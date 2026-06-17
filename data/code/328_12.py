class StringUtil:
    def get_length(self, text):
        return len(text)
if __name__ == '__main__':
    util = StringUtil()
    sample1 = "hello"
    sample2 = ""
    sample3 = "Python programming"
    print(f"Length of '{sample1}': {util.get_length(sample1)}")
    print(f"Length of '{sample2}': {util.get_length(sample2)}")
    print(f"Length of '{sample3}': {util.get_length(sample3)}")