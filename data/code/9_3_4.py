class StringCleaner:
    def clean_input(self, user_input: str) -> str:
        if not isinstance(user_input, str):
            return ""
        return user_input.strip()

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample = "   Hello World   "
    result = cleaner.clean_input(sample)
    print(result)