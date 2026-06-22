import re

def count_consonants(text):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    pattern = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')
    matches = pattern.findall(text)
    return len(matches)

if __name__ == '__main__':
    word = "Hello, World! 123 _@#"
    result = count_consonants(word)
    print(result)