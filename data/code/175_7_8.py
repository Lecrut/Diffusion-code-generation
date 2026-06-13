import re
def separate_words(sentence):
    words = []
    tokens = sentence.split()
    for token in tokens:
        if "'" in token:
            parts = token.split("'")
            if len(parts) > 1:
                words.extend(parts)
            else:
                words.append(token)
        else:
            words.append(token)
    return words
if __name__ == '__main__':
    sample_sentence1 = "I don't know where we are"
    sample_sentence2 = "She won't go, and we don't want to wait."
    sample_sentence3 = "It's a beautiful day."
    sample_sentence4 = "We don't like it's."
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