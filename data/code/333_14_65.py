import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text)
    if not matches:
        return ""
    initial_chars = ''.join(matches[:1])                                                                       
    words = text.split()
    result = [word[0] for word in words if word]
    return ''.join(result)
if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with multiple spaces."
    output = get_initial_chars(sample_text)
    print(output)