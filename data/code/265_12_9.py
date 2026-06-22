def remove_duplicates(phrase):
    seen = set()
    result = []
    for char in phrase:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_phrase1 = "Hello World"
    sample_phrase2 = "Programming is fun"
    sample_phrase3 = "AEIOUaeiou 123"
    result1 = remove_duplicates(sample_phrase1)
    result2 = remove_duplicates(sample_phrase2)
    result3 = remove_duplicates(sample_phrase3)
    print(f"'{sample_phrase1}' -> '{result1}'")
    print(f"'{sample_phrase2}' -> '{result2}'")
    print(f"'{sample_phrase3}' -> '{result3}'")