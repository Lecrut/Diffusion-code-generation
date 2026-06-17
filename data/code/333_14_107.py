import re
def extract_initial_chars(text: str) -> str:
    matches = re.findall(r'\S+', text)
    if not matches:
        return ""
    result_chars = [word[0] for word in matches]
    return "".join(result_chars)
if __name__ == '__main__':
    sample_string = "Hello world! This is a test string. Python 3.12"
    output = extract_initial_chars(sample_string)
    print(output)