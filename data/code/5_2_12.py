def capitalize_sentence(sentence):
    if not sentence:
        return ""
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    print(capitalize_sentence("hello world"))
    print(capitalize_sentence("python programming"))
    print(capitalize_sentence(""))