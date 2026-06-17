import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+'
    sentences = re.split(pattern, text.strip())
    return [sentence for sentence in sentences if sentence]
if __name__ == '__main__':
    sample_input = "Hello world! How are you? I am fine today."
    result = split_sentences(sample_input)
    print('\n'.join(result))