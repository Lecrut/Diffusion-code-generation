def get_repeated_char_counts(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = {}
    for char, count in counts.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample_string = "programming"
    print(get_repeated_char_counts(sample_string))