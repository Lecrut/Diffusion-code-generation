import re
def separate_words(sentence):
    words = []
    tokens = sentence.split()
    for token in tokens:
        if re.search(r"[a-zA-Z]+'t\b", token):
            match = re.match(r"(\w+)'t\b", token)
            if match:
                base_word = match.group(1)
                suffix = 't'
                words.append(base_word)
                words.append(suffix)
            else:
                words.append(token)
        else:
            words.append(token)
    return words
if __name__ == '__main__':
    sample_sentence1 = "I don't know where we are going"
    sample_sentence2 = "She won't go, and we can't stop."
    sample_sentence3 = "It is not easy."
    sample_sentence4 = "They don't like it."
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