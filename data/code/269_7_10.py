def remove_duplicate_punctuation(s):
    result = []
    seen = set()
    for char in s:
        if char.isalpha() or (char.isdigit() and len(result) > 0 and result[-1].isdigit()):
            result.append(char)
        elif char not in seen and not char.isspace():
            result.append(char)
            seen.add(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, world!! This is a test... string with punctuation."
    print(remove_duplicate_punctuation(sample_string))