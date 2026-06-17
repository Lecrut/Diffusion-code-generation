import re
def split_words(text):
    return [word.strip('.,!?;:"\'') for word in text.split()] if not isinstance(text, str) else re.findall(r'\b\w+\b', text.lower())
if __name__ == '__main__':
    sample = "Hello, world! This is a test. Python's regex capabilities are powerful."
    result = split_words(sample)
    print(result)