def unique_characters(phrase):
    result = []
    for i, char in enumerate(phrase):
        if i == 0 or phrase[i-1] != char:
            result.append(char)
    return result

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_characters(sample_phrase))