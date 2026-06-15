import re
def separate_words(sentence):
    words = []
    tokens = re.findall(r"[\w']+|[.,!?;]", sentence)
    for token in tokens:
        if token.isalnum() or "'" in token:
            words.append(token)
        elif token in ['.', ',', '!', '?', ';']:
            words.append(token)
        else:
            words.append(token)
    return words
def process_sentence(sentence):
    if not sentence:
        return []
    raw_tokens = sentence.split()
    final_words = []
    for token in raw_tokens:
        if re.match(r"(\w+)'t$", token):
            base_word = token[:-2]
            suffix = token[-2:]
            final_words.append(base_word)
            final_words.append(suffix)
        else:
            final_words.append(token)
    return final_words
if __name__ == '__main__':
    sample1 = "I don't know where to go."
    sample2 = "She won't; it's fine!"
    sample3 = "We are going."
    sample4 = "It's a test."
    sample5 = "They don't like it."
    print(f"Input: '{sample1}'")
    print("Output:", process_sentence(sample1))
    print("-" * 20)
    print(f"Input: '{sample2}'")
    print("Output:", process_sentence(sample2))
    print("-" * 20)
    print(f"Input: '{sample3}'")
    print("Output:", process_sentence(sample3))
    print("-" * 20)
    print(f"Input: '{sample4}'")
    print("Output:", process_sentence(sample4))
    print("-" * 20)
    print(f"Input: '{sample5}'")
    print("Output:", process_sentence(sample5))