import re
def separate_words(sentence):
    words = []
    tokens = re.findall(r"[\w']+|[.,!?;]", sentence)
    for token in tokens:
        if token.isalnum() or "'" in token:
            words.append(token)
        elif token in ['.', ',', '!', '?', ';']:
            words.append(token)
    return words
def process_sentence(sentence):
    initial_tokens = sentence.split()
    final_words = []
    for token in initial_tokens:
        if re.match(r"(\w+)'t$", token):
            base_word = token[:-2]
            suffix = token[-2:]
            final_words.append(base_word)
            final_words.append(suffix)
        else:
            final_words.append(token)
    return final_words
if __name__ == '__main__':
    sample_sentence1 = "I don't know where we are going."
    sample_sentence2 = "She won't go, and we can't stop."
    sample_sentence3 = "It is not a problem."
    sample_sentence4 = "We don't like it."
    print(f"Input: '{sample_sentence1}'")
    result1 = process_sentence(sample_sentence1)
    print(f"Output: {result1}\n")
    print(f"Input: '{sample_sentence2}'")
    result2 = process_sentence(sample_sentence2)
    print(f"Output: {result2}\n")
    print(f"Input: '{sample_sentence3}'")
    result3 = process_sentence(sample_sentence3)
    print(f"Output: {result3}\n")
    print(f"Input: '{sample_sentence4}'")
    result4 = process_sentence(sample_sentence4)
    print(f"Output: {result4}\n")