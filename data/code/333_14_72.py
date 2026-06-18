import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text)
    if not matches:
        return ""
    initial_chars = ''.join(matches[:1])                                                      
    return ''.join(word[0] for word in text.split() if len(word) > 0)
if __name__ == '__main__':
    sample_string = "Hello World Python Programming is Fun"
    result = get_initial_chars(sample_string)
    print(result)