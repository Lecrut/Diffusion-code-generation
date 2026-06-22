def get_repeated_chars(s: str) -> list:
    seen = set()
    repeated = set()
    result = []
    for char in s:
        if char in seen:
            if char not in repeated:
                repeated.add(char)
                result.append(char)
        else:
            seen.add(char)
    return result

if __name__ == '__main__':
    sample_string = "programming"
    output = get_repeated_chars(sample_string)
    print(output)