def find_repeated_chars(s):
    seen = {}
    result = []
    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for char in s:
        if seen[char] > 1 and char not in result:
            result.append(char)
    return result

if __name__ == '__main__':
    sample_string = "programming"
    output = find_repeated_chars(sample_string)
    print(output)