import re

def count_consonants(text: str) -> int:
    consonant_pattern = re.compile(r'[^aeiouAEIOU\s\d\s_]+')
    consonants = consonant_pattern.findall(text)
    return sum(len(c) for c in consonants)

if __name__ == '__main__':
    sample_text = "Hello World 123!"
    result = count_consonants(sample_text)
    print(result)