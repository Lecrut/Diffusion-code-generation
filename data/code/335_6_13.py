import re
def split_words(text: str) -> list[str]:
    return re.findall(r'\b[\w]+', text.lower())
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test... case."
    result = split_words(sample_text)
    print(result if isinstance(result, list) else [result])