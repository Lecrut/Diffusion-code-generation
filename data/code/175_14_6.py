def split_sentence(sentence):
    result = []
    word = ''
    for char in sentence:
        if char == ' ':
            if word:
                result.append(word)
                word = ''
        else:
            word += char
    if word:
        result.append(word)
    return result

if __name__ == '__main__':
    print(split_sentence('  Hello   world!'))