import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    if not matches:
        return ""
    result = ''.join(matches[:1])                                            
    return result
if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    output = get_initial_chars(sample_string)
    print(output)