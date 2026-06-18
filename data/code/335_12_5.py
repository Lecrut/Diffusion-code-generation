import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+'
    sentences = []
    current_sentence = text
    for match in re.finditer(pattern, current_sentence):
        end_index = match.start() + len(match.group())
        sentence = current_sentence[:end_index].strip()
        if sentence:
            sentences.append(sentence)
    return sentences
if __name__ == '__main__':
    sample_input = "Hello world. How are you? I am fine, thank you."
    result = split_sentences(sample_input)
    print(result)