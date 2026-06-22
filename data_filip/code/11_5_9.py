def get_repeated_chars(text):
    seen = {}
    repeated = []
    for char in text:
        if char in seen:
            if seen[char] == 1:
                repeated.append(char)
            seen[char] += 1
        else:
            seen[char] = 1
    return repeated

if __name__ == '__main__':
    sample_string = "programming"
    result = get_repeated_chars(sample_string)
    print(result)