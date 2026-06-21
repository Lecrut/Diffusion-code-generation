def get_repeated_characters(s):
    seen = set()
    repeated = []
    for char in s:
        if char in seen:
            if char not in repeated:
                repeated.append(char)
        else:
            seen.add(char)
    return repeated

if __name__ == '__main__':
    sample_string = "programming"
    result = get_repeated_characters(sample_string)
    print(result)