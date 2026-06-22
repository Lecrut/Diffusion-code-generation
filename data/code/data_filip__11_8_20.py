from collections import Counter

def find_chars_appearing_twice(s):
    counts = Counter(s)
    result = [char for char, count in counts.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_text = "aabbccddee"
    result = find_chars_appearing_twice(sample_text)
    print(result)