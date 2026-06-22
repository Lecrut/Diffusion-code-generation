def find_repeated_chars(s):
    counts = {}
    order = []
    for char in s:
        if char not in counts:
            counts[char] = 0
            order.append(char)
        counts[char] += 1
    result = []
    for char in order:
        if counts[char] > 1:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    text = "abracadabra"
    repeated = find_repeated_chars(text)
    print(repeated)