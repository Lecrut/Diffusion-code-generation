def capitalize_sentence(text):
    if not text:
        return ""
    words = text.split(' ')
    result = []
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
        else:
            result.append(word)
    return ' '.join(result)

if __name__ == '__main__':
    print(capitalize_sentence("hello world"))
    print(capitalize_sentence(""))
    print(capitalize_sentence("python programming"))