def unique_characters(phrase):
    result = []
    for char in phrase:
        if char not in result:
            result.append(char)
    return result

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_characters(sample_phrase))