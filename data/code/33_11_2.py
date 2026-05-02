class StringCleaner:
    def clean(self, text):
        if not text:
            return ""
        return text.replace(" ", "")
if __name__ == '__main__':
    cleaner = StringCleaner()
    sample1 = "Hello World"
    sample2 = "   leading and trailing spaces   "
    sample3 = "nospaceshere"
    sample4 = ""
    sample5 = "a b c d"
    print(f"'{sample1}' cleaned: '{cleaner.clean(sample1)}'")
    print(f"'{sample2}' cleaned: '{cleaner.clean(sample2)}'")
    print(f"'{sample3}' cleaned: '{cleaner.clean(sample3)}'")
    print(f"'{sample4}' cleaned: '{cleaner.clean(sample4)}'")
    print(f"'{sample5}' cleaned: '{cleaner.clean(sample5)}'")