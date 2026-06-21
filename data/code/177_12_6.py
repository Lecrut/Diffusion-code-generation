def split_string(s):
    result = []
    word = ''
    for char in s:
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
    print(split_string("Hello world this is a test"))