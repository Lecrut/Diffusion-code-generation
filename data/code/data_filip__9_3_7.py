class UserInputValidator:
    def clean(self, text):
        if text is None:
            return ""
        return text.strip()

if __name__ == "__main__":
    validator = UserInputValidator()
    sample_input = "   invalid user data   "
    result = validator.clean(sample_input)
    print(result)