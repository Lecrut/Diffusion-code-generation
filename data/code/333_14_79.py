import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    matches = [m.group(0)[0] for m in re.finditer(r'\S', ' '.join(words))]
    return ''.join(matches)
if __name__ == '__main__':
    sample_string = "Hello world! Python is awesome. How are you today?"
    result = get_initial_chars(sample_string)
    print(result)