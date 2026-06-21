def split_sentence(sentence):
    words = []
    start = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            if start < i:
                words.append(sentence[start:i])
            start = i + 1
    if start < len(sentence):
        words.append(sentence[start:])
    return words

if __name__ == '__main__':
    print(split_sentence("   Hello World! This is a test. "))
    print(split_sentence("NoSpacesHere"))
    print(split_sentence("  Leading and trailing spaces  "))