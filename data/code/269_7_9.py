def remove_duplicate_punctuation(s):
    result = []
    seen = set()
    for char in s:
        if char.isalpha() or char.isdigit():
            result.append(char)
            seen.clear()
        elif char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test... Test."
    print(remove_duplicate_punctuation(sample_string))