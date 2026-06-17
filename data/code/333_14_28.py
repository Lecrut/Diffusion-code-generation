import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    result = []
    for word in words:
        char_match = re.match(r'^\w', word)
        if char_match and len(word) > 0:
            first_char = char_match.group(0)[0]
            result.append(first_char)
        else:
            result.append(word[0])
    return "".join(result)
if __name__ == '__main__':
    sample_string = "Hello World Python Programming is Fun"
    output = get_initial_chars(sample_string)
    print(output)