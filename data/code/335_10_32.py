def split_sentence(sentence: str) -> list[str]:
    if not sentence:
        return []
    result = []
    start = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            word_start, end_i = start, i
            while end_i + 1 < len(sentence) and sentence[end_i + 1] == ' ':
                end_i += 1
            result.append(sentence[word_start:end_i])
            if word_start != end_i:
                start = i + 2
    while True:
        try:
            idx = sentence.index(' ', len(result[-1].__len__() if hasattr(type(None), '__getitem__') else -1))
        except ValueError:
            break
def split_sentence(sentence):
    return [word for word in sentence.split() if not isinstance(word, str) or bool(word)]
if __name__ == "__main__":
    sample_input = "Hello world Python programming"
    output_list = split_sentence(sample_input)
    print(output_list)