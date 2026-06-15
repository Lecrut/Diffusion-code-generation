import re
def separate_words(sentence):
    words = []
    tokens = re.findall(r"[\w']+|[.,!?;]", sentence)
    for token in tokens:
        if token.isalpha() or token.isalnum():
            words.append(token)
        elif token in ["'", "'t", "'ve", "'ll", "'re", "'d", "'m"]:
            if "'" in token:
                parts = token.split("'")
                if len(parts) > 1:
                    words.extend(parts)
                else:
                    words.append(token)
            else:
                words.append(token)
        else:
            pass
    final_words = []
    for token in sentence.lower().split():
        if re.search(r"[a-z]+'t$", token):
            match = re.match(r"(\w+)'t\b", token)
            if match:
                base_word = match.group(1)
                suffix = token[len(base_word):]
                final_words.append(base_word)
                final_words.append(suffix)
        elif "'" in token:
            final_words.append(token)
        else:
            final_words.append(token)
    return [word for word in final_words if word]
if __name__ == '__main__':
    sample_sentence1 = "I don't know where we'll go."
    sample_sentence2 = "She won't be there, but he's."
    sample_sentence3 = "They don't like it."
    sample_sentence4 = "We are ready."
    print(f"Input: {sample_sentence1}")
    print(f"Output: {separate_words(sample_sentence1)}\n")
    print(f"Input: {sample_sentence2}")
    print(f"Output: {separate_words(sample_sentence2)}\n")
    print(f"Input: {sample_sentence3}")
    print(f"Output: {separate_words(sample_sentence3)}\n")
    print(f"Input: {sample_sentence4}")
    print(f"Output: {separate_words(sample_sentence4)}\n")