def remove_duplicates(phrase):
    seen = set()
    result = []
    for char in phrase:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(remove_duplicates(sample_phrase))