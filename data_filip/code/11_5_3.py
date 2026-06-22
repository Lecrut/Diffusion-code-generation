def detect_repeated_characters(s):
    seen = set()
    repeated = []
    for char in s:
        if char in seen and char not in repeated:
            repeated.append(char)
        else:
            seen.add(char)
    return repeated

if __name__ == '__main__':
    sample = "programming"
    result = detect_repeated_characters(sample)
    print(result)