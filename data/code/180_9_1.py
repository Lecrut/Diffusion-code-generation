class StringChecker:
    def __init__(self, main_string):
        self.main_string = main_string
    def is_substring(self, sub_string):
        return sub_string in self.main_string
if __name__ == '__main__':
    text1 = "hello world"
    text2 = "world"
    text3 = "python"
    text4 = "java"
    checker1 = StringChecker(text1)
    print(f"Is '{text2}' a substring of '{text1}'? {checker1.is_substring(text2)}")
    checker2 = StringChecker(text3)
    print(f"Is '{text4}' a substring of '{text3}'? {checker2.is_substring(text4)}")