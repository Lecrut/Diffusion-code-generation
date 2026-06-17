import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    if not matches:
        return ""
    result_chars = [match[0] for match in matches]
    return ''.join(result_chars)
if __name__ == '__main__':
    sample_text = "Hello World! Python Programming is Fun and Awesome."
    output_string = get_initial_chars(sample_text)
    print(output_string)