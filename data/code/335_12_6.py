import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+'
    return [sentence.strip() for sentence in re.split(pattern, text)]
if __name__ == '__main__':
    sample_text = "Hello world! How are you? I am fine thanks."
    sentences = split_sentences(sample_text)
    print('\n'.join(sentences))