def find_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    seen.clear()
    result = []
    for char in s:
        if char in repeated and char not in seen:
            result.append(char)
            seen.add(char)
    return result

if __name__ == '__main__':
    sample_string = "programming"
    output = find_repeated_characters(sample_string)
    print(output)