import re
class TextProcessor:
    def count_words(self, text):
        return len(re.findall(r'\w+', text))
    def remove_special_chars(self, text):
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)
    def extract_numbers(self, text):
        return [int(x) for x in re.findall(r'\d+', text)]
    def reverse_string_case(self, text):
        return ''.join(c.lower() if c.isupper() else c.upper() for c in reversed(text))
if __name__ == '__main__':
    sample_text = "Hello! How are you? I have 3 apples and 5 oranges. Don't worry about the special chars @#$%^&*()."
    processor = TextProcessor()
    print(f"Word count: {processor.count_words(sample_text)}")
    cleaned = processor.remove_special_chars(sample_text)
    print("Cleaned text:", repr(cleaned))
    numbers = processor.extract_numbers(sample_text)
    print("Extracted numbers:", numbers)
    reversed_case = processor.reverse_string_case(sample_text)
    print("Reversed case:", reversed_case)