def split_string(s):
    result = []
    word = []
    for char in s:
        if char == ' ':
            if word:
                result.append(''.join(word))
                word = []
        else:
            word.append(char)
    if word:
        result.append(''.join(word))
    return result

if __name__ == '__main__':
    sample_string = "Hello world this is a test"
    print(split_string(sample_string))