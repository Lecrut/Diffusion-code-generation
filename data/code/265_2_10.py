def unique_chars(phrase):
    seen = set()
    result = []
    for char in phrase:
        if char not in seen:
            if char not in result:
                result.append(char)
            seen.add(char)
    return ''.join(result)

if __name__ == '__main__':
    print(unique_chars("programming"))