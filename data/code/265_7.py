def count_characters(phrase):
    counts = {}
    for char in phrase:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
if __name__ == '__main__':
    sample_phrase = "hello world"
    result = count_characters(sample_phrase)
    print(result)