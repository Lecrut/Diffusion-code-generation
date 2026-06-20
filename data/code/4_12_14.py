import re

def count_consonants(text):
    return len(re.findall(r'(?i)[b-df-hj-np-tv-z]', text))

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    print(count_consonants(test_string))