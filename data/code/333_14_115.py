import re
def get_initial_chars(s):
    matches = re.findall(r'\b\w', s)
    if not matches:
        return ""
    initial_chars = ''.join(matches[:1])                                                                                    
    words = re.findall(r'\b\w+', s)
    result = [word[0] for word in words if len(word) > 0]
    return ''.join(result)
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with multiple words."
    output = get_initial_chars(sample_string)
    print(output)