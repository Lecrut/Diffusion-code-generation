def run_length_encode(text):
    if not text:
        return ""
    return "".join([f"{count}{char}" for char, count in __group_chars(text)])

def __group_chars(text):
    groups = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            groups.append((current_char, count))
            current_char = char
            count = 1
    groups.append((current_char, count))
    return groups

if __name__ == '__main__':
    long_string = "AAAABBBCCDAA"
    result = run_length_encode(long_string)
    print(result)