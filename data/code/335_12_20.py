import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+(?=\w)'
    return [sentence.strip() for sentence in re.split(pattern, text)]
if __name__ == '__main__':
    sample_text = "Hello world! How are you today? I am fine and ready to work."
    sentences = split_sentences(sample_text)
    print('\n'.join(sentences))