def find_chars_exactly_twice(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = sorted(char for char, count in counts.items() if count == 2)
    return result

if __name__ == '__main__':
    print(find_chars_exactly_twice("hello world"))