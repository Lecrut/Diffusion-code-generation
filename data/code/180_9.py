class StringChecker:
    def is_substring(self, main_string, sub_string):
        return sub_string in main_string
if __name__ == '__main__':
    checker = StringChecker()
    text = "hello world"
    substring1 = "world"
    substring2 = "hello"
    substring3 = "goodbye"
    print(f"Is '{substring1}' a substring of '{text}'? {checker.is_substring(text, substring1)}")
    print(f"Is '{substring2}' a substring of '{text}'? {checker.is_substring(text, substring2)}")
    print(f"Is '{substring3}' a substring of '{text}'? {checker.is_substring(text, substring3)}")