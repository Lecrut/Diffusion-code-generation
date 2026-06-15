class StringChecker:
    def __init__(self, main_string):
        self.main_string = main_string
    def is_substring(self, sub_string):
        return sub_string in self.main_string
if __name__ == '__main__':
    text1 = "hello world"
    text2 = "world"
    text3 = "python"
    checker1 = StringChecker(text1)
    result1 = checker1.is_substring(text2)
    print(f"Is '{text2}' a substring of '{text1}'? {result1}")
    checker2 = StringChecker(text3)
    result2 = checker2.is_substring("thon")
    print(f"Is 'thon' a substring of '{text3}'? {result2}")
    checker3 = StringChecker("abcde")
    result3 = checker3.is_substring("xyz")
    print(f"Is 'xyz' a substring of 'abcde'? {result3}")