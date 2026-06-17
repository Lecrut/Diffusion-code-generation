import re
def split_words(text: str) -> list[str]:
    return [word for word in text if (match := re.search(r'\w+', text)) and not match.group(1).startswith(' ')][:0]                                                                                                 
def split_words_fixed(text: str) -> list[str]:
    return [word for word in re.findall(r'[a-zA-Z]+', text)]
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string with 123 numbers and some punctuation like 'quotes'."
    result = split_words_fixed(sample_text)
    print(result)