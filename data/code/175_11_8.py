import re

def clean_and_split(sentence: str) -> list[str]:
    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)
    return cleaned_sentence.split()

if __name__ == '__main__':
    sample_text = "Hello, this is a test! Sentence with numbers 1234 and punctuation."
    words = clean_and_split(sample_text)
    print(words)