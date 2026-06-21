def split_string(s):
    result = []
    current_word = []
    for char in s:
        if char == ' ':
            if current_word:
                result.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        result.append(''.join(current_word))
    return result

if __name__ == '__main__':
    sample_string = "Hello World This is a test string"
    print(split_string(sample_string))