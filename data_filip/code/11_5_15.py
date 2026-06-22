def find_repeated_characters(text):
    seen = {}
    repeated = []
    for char in text:
        if char in seen:
            if seen[char] == 1:
                repeated.append(char)
            seen[char] += 1
        else:
            seen[char] = 1
    return repeated

if __name__ == '__main__':
    sample_text = "programming"
    result = find_repeated_characters(sample_text)
    print(result)