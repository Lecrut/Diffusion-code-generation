class TokenExtractor:
    @staticmethod
    def find_initial_token(text: str) -> str:
        if not text:
            return ""
        match = re.match(r"(\S+)", text)
        if match:
            return match.group(1)
        return ""

if __name__ == '__main__':
    sample_text_1 = "Hello world, this is a test."
    sample_text_2 = "  \t\n\rThis starts with whitespace."
    sample_text_3 = "123 numbers and symbols."
    sample_text_4 = ""
    sample_text_5 = "   "
    print(f"Input: '{sample_text_1}' -> Initial Token: '{TokenExtractor.find_initial_token(sample_text_1)}'")
    print(f"Input: '{sample_text_2}' -> Initial Token: '{TokenExtractor.find_initial_token(sample_text_2)}'")
    print(f"Input: '{sample_text_3}' -> Initial Token: '{TokenExtractor.find_initial_token(sample_text_3)}'")
    print(f"Input: '{sample_text_4}' -> Initial Token: '{TokenExtractor.find_initial_token(sample_text_4)}'")