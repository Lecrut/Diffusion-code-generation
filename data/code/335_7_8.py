import re
def extract_words(sentence: str) -> list[str]:
    return [word for word in re.findall(r'\b\w+\b', sentence)]
if __name__ == '__main__':
    sample = "Hello, world! This is a test."
    result = extract_words(sample)
    print(result)