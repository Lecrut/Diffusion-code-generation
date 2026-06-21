def split_string(s):
    result = []
    current_word = ''
    for char in s:
        if char == ' ':
            if current_word:
                result.append(current_word)
                current_word = ''
        else:
            current_word += char
    if current_word:
        result.append(current_word)
    return result

if __name__ == '__main__':
    sample_string = "Hello world this is a test"
    print(split_string(sample_string))