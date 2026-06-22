def find_characters_appearing_twice(s):
    from collections import Counter
    counts = Counter(s)
    result = [char for char, count in counts.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    text = "programming"
    chars = find_characters_appearing_twice(text)
    print(chars)