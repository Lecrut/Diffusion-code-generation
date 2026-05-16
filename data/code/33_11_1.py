class StringCleaner:
    def clean(self, text):
        if not text:
            return ""
        return text.replace(" ", "")
if __name__ == '__main__':
    cleaner = StringCleaner()
    sample1 = "Hello World"
    sample2 = "   leading and trailing spaces   "
    sample3 = ""
    sample4 = "nospaceshere"
    result1 = cleaner.clean(sample1)
    result2 = cleaner.clean(sample2)
    result3 = cleaner.clean(sample3)
    result4 = cleaner.clean(sample4)
    print(f"Input: '{sample1}', Output: '{result1}'")
    print(f"Input: '{sample2}', Output: '{result2}'")
    print(f"Input: '{sample3}', Output: '{result3}'")
    print(f"Input: '{sample4}', Output: '{result4}'")