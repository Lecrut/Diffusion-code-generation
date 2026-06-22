def unique_characters(phrase):
    seen = set()
    result = []
    for char in phrase:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return result

if __name__ == '__main__':
    sample_phrase1 = "hello world"
    sample_phrase2 = "programming is fun"
    print(unique_characters(sample_phrase1))
    print(unique_characters(sample_phrase2))