import re
def split_sentences(text: str) -> list[str]:
    return [sentence.strip() for sentence in text.split('.')] if '.' not in text else [s.rstrip('.') for s in text.replace('.', ' ').split()]
if __name__ == '__main__':
    sample = "Hello world. How are you? I am fine! Thank you."
    sentences = split_sentences(sample)
    print('\n'.join(sentences))