import re

def count_consonants(text: str) -> int:
    consonants = re.findall(r'[b-df-hj-np-tv-z]', text.lower())
    return len(consonants)

if __name__ == '__main__':
    test_string = "Hello World!"
    result = count_consonants(test_string)
    print(result)