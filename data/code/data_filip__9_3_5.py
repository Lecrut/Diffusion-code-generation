class InputCleaner:
    def clean(self, user_input):
        if user_input is None:
            return None
        return user_input.strip()

if __name__ == '__main__':
    cleaner = InputCleaner()
    sample_data = "   user data with spaces   "
    result = cleaner.clean(sample_data)
    print(result)