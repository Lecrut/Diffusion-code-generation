def count_characters(phrase):
    char_counts = {}
    for char in phrase:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
if __name__ == '__main__':
    sample_phrase = "hello world"
    result = count_characters(sample_phrase)
    print(result)