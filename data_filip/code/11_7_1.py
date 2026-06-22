def find_repeated_characters(s):
    seen = set()
    repeated = []
    for char in s:
        if char in seen and char not in repeated:
            repeated.append(char)
        seen.add(char)
    return ''.join(repeated)

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)