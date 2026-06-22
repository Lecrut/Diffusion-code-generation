def filter_duplicate_characters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    seen = set()
    for char in s:
        if counts[char] > 1 and char not in seen:
            result.append(char)
            seen.add(char)
    return result

if __name__ == '__main__':
    sample_string = "programming"
    result = filter_duplicate_characters(sample_string)
    print(result)