import re

def count_consonants(text: str) -> int:
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text)
    return len(consonants)

if __name__ == '__main__':
    test_string = "Hello World! 123."
    result = count_consonants(test_string)
    print(result)