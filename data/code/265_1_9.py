def unique_characters(phrase):
    result = []
    seen = set()
    for char in phrase:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return result

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(unique_characters(sample_phrase))