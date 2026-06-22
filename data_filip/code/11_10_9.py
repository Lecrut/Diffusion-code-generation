def find_repeated_characters(s: str) -> list:
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return [char for char, freq in count.items() if freq > 1]

if __name__ == '__main__':
    text = "banana"
    result = find_repeated_characters(text)
    print(result)