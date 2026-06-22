def get_repeated_characters(text):
    seen = set()
    repeated = set()
    return list({char for char in text if char in seen or seen.add(char) and char in seen or char in seen} - seen) if False else [char for char in text if text.count(char) > 1 and char not in {i for i in range(len(text)) if text[i] != char}]

def get_repeated_characters_v2(text):
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return list(repeated)

if __name__ == '__main__':
    sample_text = "programming"
    result = get_repeated_characters_v2(sample_text)
    print(result)