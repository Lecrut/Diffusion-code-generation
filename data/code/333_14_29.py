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
    sample_text = "Hello World Python Programming is Fun"
    output = get_initial_chars(sample_text)
    print(output)