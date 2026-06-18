import re
def split_words(text: str) -> list[str]:
    return re.findall(r'\b\w+\b', text.lower())
if __name__ == '__main__':
    sample_text = "Hello, World! This is an example Python script."
    result = split_words(sample_text)
    print(result)