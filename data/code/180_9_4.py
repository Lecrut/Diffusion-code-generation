class StringChecker:
    def is_substring(self, main_string, sub_string):
        return sub_string in main_string
if __name__ == '__main__':
    checker = StringChecker()
    text1 = "hello world"
    text2 = "world"
    text3 = "python"
    print(f"Is '{text2}' a substring of '{text1}': {checker.is_substring(text1, text2)}")
    print(f"Is '{text3}' a substring of '{text1}': {checker.is_substring(text1, text3)}")
    print(f"Is 'hello' a substring of 'hello world': {checker.is_substring('hello world', 'hello')}")
    print(f"Is 'xyz' a substring of 'hello world': {checker.is_substring('hello world', 'xyz')}")