import re
def split_words(text: str) -> list[str]:
    return [word.strip(".,!?;:'\"") for word in text.split()] if not isinstance(text, str) else re.findall(r"\b[\w']+\b", text)
if __name__ == "__main__":
    sample = "Hello, world! This is a test. How are you?"
    result = split_words(sample)
    print(result)