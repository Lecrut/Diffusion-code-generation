import re

def count_consonants(text):
    pattern = r'[^aeiouAEIOU\W\d_]'
    matches = re.findall(pattern, text)
    return len(matches)

if __name__ == '__main__':
    sample = "Hello, World! 123"
    result = count_consonants(sample)
    print(result)