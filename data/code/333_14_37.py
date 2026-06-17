import re
def get_initial_chars(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    result_parts = []
    for word in words:
        match = re.match(r'^\S', word)
        if match:
            result_parts.append(match.group(0))
    return "".join(result_parts)
if __name__ == '__main__':
    sample_text = "Hello World Python Programming is Fun and Easy"
    output = get_initial_chars(sample_text)
    print(output)