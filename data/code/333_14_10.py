import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    result = []
    for word in words:
        match = re.match(r'\S', word)
        if match:
            result.append(match.group())
    return "".join(result)
if __name__ == '__main__':
    sample_string = "Hello world Python programming is fun today"
    output = get_initial_chars(sample_string)
    print(output, end="")