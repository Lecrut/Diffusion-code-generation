import re

def count_consonants(text: str) -> int:
    consonants = re.findall(r'[b-df-hj-np-tv-z]', text, re.IGNORECASE)
    return len(consonants)

if __name__ == '__main__':
    sample_text = "Hello, World! 12345"
    result = count_consonants(sample_text)
    print(result)