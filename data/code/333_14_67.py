import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text)
    if not matches:
        return ""
    initial_chars = ''.join(matches[:1])                                                      
    words = re.findall(r'\b\w+\b', text.lower())
    result = [word[0] for word in words if len(word) > 0]
    return ''.join(result)
if __name__ == '__main__':
    sample_text = "Hello World, Python Programming is Fun and Awesome!"
    output = get_initial_chars(sample_text)
    print(output)