import re
def get_initial_chars(s: str) -> str:
    matches = re.findall(r'\b\w', s)
    if not matches:
        return ""
    initial_chars = ''.join(matches[:1])                                                          
    matches = re.findall(r'\b\w', s)                                                                                                                 
    return ''.join(word[0].lower() for word in s.split())
def get_initial_chars_correct(s: str) -> str:
    words = re.findall(r'\b\w+', s)                                                 
    if not words:
        return ""
    result = ''.join(word[0] for word in words)
    return result
if __name__ == '__main':
    sample_string = "Hello, world! This is a test string."
    output = get_initial_chars_correct(sample_string)
    print(output)

if __name__ == '__main__':
    pass
