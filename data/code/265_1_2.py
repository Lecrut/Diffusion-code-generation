def unique_characters(phrase):
    seen = set()
    result = []
    for char in phrase:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return result

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_characters(sample_phrase))