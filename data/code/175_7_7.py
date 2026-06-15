import re
def separate_words(sentence):
    tokens = []
    for word in sentence.split():
        if re.search(r"[a-zA-Z]+$", word):
            tokens.append(word)
        else:
            parts = re.findall(r"([a-zA-Z]+)([^a-zA-Z]*)$", word)
            if parts:
                tokens.extend(parts)
            else:
                tokens.append(word)
    return tokens
if __name__ == '__main__':
    sample_sentence1 = "I don't know where we are going"
    sample_sentence2 = "She won't go, and we don't want to wait."
    sample_sentence3 = "This is a simple test."
    sample_sentence4 = "It's a difficult problem."
    result1 = separate_words(sample_sentence1)
    result2 = separate_words(sample_sentence2)
    result3 = separate_words(sample_sentence3)
    result4 = separate_words(sample_sentence4)
    print(f"Input: '{sample_sentence1}'")
    print(f"Output: {result1}\n")
    print(f"Input: '{sample_sentence2}'")
    print(f"Output: {result2}\n")
    print(f"Input: '{sample_sentence3}'")
    print(f"Output: {result3}\n")
    print(f"Input: '{sample_sentence4}'")
    print(f"Output: {result4}\n")