import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    return ''.join(matches)
if __name__ == '__main__':
    sample_string = "Hello World! Python Programming is Fun."
    result = get_initial_chars(sample_string)
    print(result)