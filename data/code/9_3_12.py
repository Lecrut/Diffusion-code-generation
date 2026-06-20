class UserInputCleaner:
    def clean(self, text):
        if text is None:
            return None
        return text.strip()

if __name__ == '__main__':
    sample_inputs = ["  hello world  ", "   \t\n", "no_spaces", None, "\t  \n  python  \n  "]
    cleaner = UserInputCleaner()
    for raw in sample_inputs:
        result = cleaner.clean(raw)
        print(result)