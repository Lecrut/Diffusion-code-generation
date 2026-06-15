class StringChecker:
    def is_substring(self, main_string: str, sub_string: str) -> bool:
        return sub_string in main_string
if __name__ == '__main__':
    checker = StringChecker()
    text1 = "hello world"
    text2 = "world"
    text3 = "python"
    text4 = "java"
    print(f"Is '{text2}' a substring of '{text1}': {checker.is_substring(text1, text2)}")
    print(f"Is '{text4}' a substring of '{text1}': {checker.is_substring(text1, text4)}")
    print(f"Is '{text3}' a substring of '{text1}': {checker.is_substring(text1, text3)}")
    print(f"Is 'hello' a substring of 'hello world': {checker.is_substring('hello world', 'hello')}")
    print(f"Is '' a substring of 'some string': {checker.is_substring('some string', '')}")