import re
def separate_words(sentence):
    tokens = []
    matches = re.findall(r"[\w']+", sentence)
    for match in matches:
        if "'" in match:
            parts = match.split("'")
            if len(parts) == 2:
                tokens.extend(parts)
            else:
                tokens.append(match)
        else:
            tokens.append(match)
    return tokens
if __name__ == '__main__':
    sample_sentence1 = "I don't know where the time is"
    sample_sentence2 = "She won't go if you don't help"
    sample_sentence3 = "We don't like that"
    sample_sentence4 = "It's a beautiful day"
    sample_sentence5 = "He didn't see it"
    print(f"Original: '{sample_sentence1}'")
    result1 = separate_words(sample_sentence1)
    print(f"Result: {result1}\n")
    print(f"Original: '{sample_sentence2}'")
    result2 = separate_words(sample_sentence2)
    print(f"Result: {result2}\n")
    print(f"Original: '{sample_sentence3}'")
    result3 = separate_words(sample_sentence3)
    print(f"Result: {result3}\n")
    print(f"Original: '{sample_sentence4}'")
    result4 = separate_words(sample_sentence4)
    print(f"Result: {result4}\n")
    print(f"Original: '{sample_sentence5}'")
    result5 = separate_words(sample_sentence5)
    print(f"Result: {result5}\n")