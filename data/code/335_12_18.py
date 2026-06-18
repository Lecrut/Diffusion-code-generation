import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+'
    return [sentence.strip() for sentence in re.split(pattern, text)] if text else []
if __name__ == '__main__':
    sample_input = "Hello world! How are you? I am fine and working on a script."
    sentences = split_sentences(sample_input)
    print('\n'.join(sentences))