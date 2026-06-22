def filter_repeated_characters(text):
    if not text:
        return ""
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    seen = set()
    for char in text:
        if counts[char] > 1 and char not in seen:
            result.append(char)
            seen.add(char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "programming"
    output = filter_repeated_characters(sample_string)
    print(output)