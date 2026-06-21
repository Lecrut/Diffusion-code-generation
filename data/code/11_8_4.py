def find_chars_appearing_twice(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = [char for char, count in counts.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample = "hello world"
    print(find_chars_appearing_twice(sample))