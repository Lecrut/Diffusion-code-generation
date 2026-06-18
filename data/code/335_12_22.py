import re
def split_sentences(text: str) -> list[str]:
    pattern = r'[.!?]+(?=[\s]|$)'
    return [sent.strip() for sent in re.split(pattern, text)]
if __name__ == '__main__':
    sample_text = "Hello world! How are you? I am fine and working on a script."
    sentences = split_sentences(sample_text)
    print('\n'.join(sentences))