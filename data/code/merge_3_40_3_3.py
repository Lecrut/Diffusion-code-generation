import re

def extract_initials(text: str) -> str:
    return ' '.join(word[0] if word else '' for word in re.findall(r'\b[a-zA-Z]+\b', text))

if __name__ == '__main__':
    sample = "Hello World! Python is great."
    result = extract_initials(sample)
    print(result)