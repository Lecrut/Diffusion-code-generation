import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+'
    return re.split(pattern, text.strip())
if __name__ == '__main__':
    sample_text = "Hello world! How are you? I am fine, thank you."
    sentences = split_sentences(sample_text)
    for sentence in sentences:
        print(sentence)