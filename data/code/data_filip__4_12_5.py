import re

def count_consonants(text: str) -> int:
    consonants = re.findall('[^aeiouAEIOU\\s0-9\\W]', text)
    return len(consonants)
if __name__ == '__main__':
    sample_text = 'Hello, World! 123'
    result = count_consonants(sample_text)
    print(result)