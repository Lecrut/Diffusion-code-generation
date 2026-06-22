def find_repeated_chars(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    repeated = [char for char, count in freq.items() if count > 1]
    return repeated

if __name__ == '__main__':
    print(find_repeated_chars("hello"))
    print(find_repeated_chars("world"))
    print(find_repeated_chars("aabbcc"))
    print(find_repeated_chars("abcdef"))
    print(find_repeated_chars("programming"))