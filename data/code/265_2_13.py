def unique_chars(phrase):
    seen = set()
    result = []
    for char in phrase:
        if char not in seen:
            seen.add(char)
            result.append(char)
        elif char in result:
            result.remove(char)
    return ''.join(result)

if __name__ == '__main__':
    print(unique_chars("programming"))