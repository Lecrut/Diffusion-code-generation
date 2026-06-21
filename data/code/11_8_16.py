def find_chars_appearing_twice(s):
    from collections import Counter
    counts = Counter(s)
    result = sorted([char for char, count in counts.items() if count == 2])
    return result

if __name__ == '__main__':
    sample_string = "hello world"
    print(find_chars_appearing_twice(sample_string))