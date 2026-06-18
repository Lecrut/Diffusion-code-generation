import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+(?=\w)'
    return [sent.strip() for sent in text.split(pattern)] if text else []
if __name__ == '__main__':
    sample_text = "Hello world! How are you today?"
    sentences = split_sentences(sample_text)
    print('\n'.join(sentences))