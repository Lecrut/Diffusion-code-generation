def find_repeated_characters(text):
    seen = set()
    repeated = []
    for char in text:
        if char in seen and char not in repeated:
            repeated.append(char)
        else:
            seen.add(char)
    return repeated

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)