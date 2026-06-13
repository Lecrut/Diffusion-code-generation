import re
def separate_words(sentence):
    words = []
    tokens = sentence.split()
    for token in tokens:
        if "'" in token:
            parts = re.split(r"'", token)
            contraction_splits = []
            if token.endswith("'t"):
                base = token[:-2]
                contraction_splits.append(base)
                contraction_splits.append("'t")
            elif token.endswith("'ve"):
                base = token[:-3]
                contraction_splits.append(base)
                contraction_splits.append("'ve")
            elif token.endswith("'re"):
                base = token[:-3]
                contraction_splits.append(base)
                contraction_splits.append("'re")
            else:
                words.append(token)
                continue
            if contraction_splits:
                words.extend(contraction_splits)
        else:
            words.append(token)
    return words
if __name__ == '__main__':
    sentence1 = "I don't know where we'll go."
    sentence2 = "She hasn't seen anything, but he won't."
    sentence3 = "This is a simple sentence."
    sentence4 = "We don't understand that."
    print(f"Original: '{sentence1}'")
    result1 = separate_words(sentence1)
    print(f"Separated: {result1}\n")
    print(f"Original: '{sentence2}'")
    result2 = separate_words(sentence2)
    print(f"Separated: {result2}\n")
    print(f"Original: '{sentence3}'")
    result3 = separate_words(sentence3)
    print(f"Separated: {result3}\n")
    print(f"Original: '{sentence4}'")
    result4 = separate_words(sentence4)
    print(f"Separated: {result4}\n")