def filter_repeated_chars(text: str) -> list:
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in text:
        if counts[char] > 1:
            if char not in result:
                result.append(char)
    return result

if __name__ == '__main__':
    sample_text = "programming"
    print(filter_repeated_chars(sample_text))