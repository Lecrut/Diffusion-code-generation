def run_length_encode(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return ''.join(encoded)

if __name__ == '__main__':
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("bbbaaa"))